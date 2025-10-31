# -*- coding: utf-8 -*-
"""Frontend Routes

All public-facing routes for visitors
"""

import logging

from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from jinja2.exceptions import TemplateNotFound
from pydantic import BaseModel, EmailStr, ValidationError
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models import ColumnType
from app.models.contact import ContactMessage
from app.schemas.requests import ContactFormRequest
from app.services import post_service, product_service, site_service
from app.utils.template_helpers import (
    get_navigation,
    post_list,
    product_list,
    site_info,
)

logger = logging.getLogger("docms")

router = APIRouter()
templates = Jinja2Templates(directory=str(settings.template_dir))


class ContactForm(BaseModel):
    """Contact form data model"""

    name: str
    email: EmailStr
    phone: str = ""
    subject: str
    message: str


# Add template helper functions to Jinja2 globals
templates.env.globals.update(
    {
        "product_list": product_list,
        "post_list": post_list,
        "site_info": site_info,
        "get_navigation": get_navigation,
    }
)


def get_base_context(request: Request, db: Session) -> dict:
    """
    Get base template context

    Args:
        request: FastAPI request object
        db: Database session

    Returns:
        Dictionary with base context variables
    """
    return {
        "request": request,
        "db": db,
        "site_settings": site_service.get_all_site_settings(db),
        "navigation": site_service.get_navigation(db),
    }


@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request, db: Session = Depends(get_db)):
    """Homepage"""
    context = get_base_context(request, db)

    # Get homepage column
    home_column = site_service.get_column_by_slug(db, "home")
    if home_column and home_column.column_type == ColumnType.SINGLE_PAGE:
        page = site_service.get_single_page(db, home_column.id)
        context["page"] = page

    # Get recommended products and posts for homepage
    context["featured_products"] = product_service.get_products(
        db, is_recommended=True, limit=6
    )
    context["featured_posts"] = post_service.get_posts(db, is_recommended=True, limit=3)

    return templates.TemplateResponse("home.html", context)


@router.get("/{column_slug}", response_class=HTMLResponse)
async def column_page(
    column_slug: str, request: Request, db: Session = Depends(get_db)
):
    """Column page (product list, post list, or single page)"""
    column = site_service.get_column_by_slug(db, column_slug)

    if not column:
        raise HTTPException(status_code=404, detail="Page not found")

    context = get_base_context(request, db)
    context["column"] = column

    # Handle different column types
    if column.column_type == ColumnType.SINGLE_PAGE:
        page = site_service.get_single_page(db, column.id)
        if not page:
            raise HTTPException(status_code=404, detail="Page not found")

        context["page"] = page

        # Check for custom template (e.g., about.html, contact.html)
        try:
            return templates.TemplateResponse(f"{column_slug}.html", context)
        except TemplateNotFound:
            logger.debug(
                f"Custom template {column_slug}.html not found, using default single_page.html"
            )
            return templates.TemplateResponse("single_page.html", context)

    elif column.column_type == ColumnType.PRODUCT:
        # Get category filter from query params
        category_id = request.query_params.get("category")
        if category_id:
            try:
                category_id = int(category_id)
            except (ValueError, TypeError):
                category_id = None

        categories = product_service.get_product_categories(db, column.id)
        products = product_service.get_products(
            db, column_id=column.id, category_id=category_id
        )

        context["categories"] = categories
        context["products"] = products
        context["current_category_id"] = category_id
        context["total"] = product_service.get_product_count(
            db, column_id=column.id, category_id=category_id
        )

        # Check for custom template (e.g., products.html)
        try:
            return templates.TemplateResponse(f"{column_slug}.html", context)
        except TemplateNotFound:
            logger.debug(
                f"Custom template {column_slug}.html not found, using default product_list.html"
            )
            return templates.TemplateResponse("product_list.html", context)

    elif column.column_type == ColumnType.POST:
        # Get category filter from query params
        category_id = request.query_params.get("category")
        if category_id:
            try:
                category_id = int(category_id)
            except (ValueError, TypeError):
                category_id = None

        categories = post_service.get_post_categories(db, column.id)
        posts = post_service.get_posts(db, column_id=column.id, category_id=category_id)

        # Get additional data for sidebar
        popular_posts = post_service.get_popular_posts(db, column.id, limit=5)
        category_stats = post_service.get_category_stats(db, column.id)
        popular_tags = post_service.get_popular_tags(db, column.id, limit=20)

        context["categories"] = categories
        context["posts"] = posts
        context["current_category_id"] = category_id
        context["total"] = post_service.get_post_count(
            db, column_id=column.id, category_id=category_id
        )
        context["popular_posts"] = popular_posts
        context["category_stats"] = category_stats
        context["popular_tags"] = popular_tags

        # Check for custom template
        try:
            return templates.TemplateResponse(f"{column_slug}.html", context)
        except TemplateNotFound:
            logger.debug(
                f"Custom template {column_slug}.html not found, using default post_list.html"
            )
            return templates.TemplateResponse("post_list.html", context)

    elif column.column_type == ColumnType.CUSTOM:
        # For custom columns like Home, try to render custom template
        # If home slug, redirect to homepage
        if column_slug == "home":
            from fastapi.responses import RedirectResponse

            return RedirectResponse(url="/", status_code=302)

        # For other custom columns, try custom template
        try:
            return templates.TemplateResponse(f"{column_slug}.html", context)
        except TemplateNotFound:
            logger.warning(
                f"Custom template {column_slug}.html not found for custom column"
            )
            raise HTTPException(status_code=404, detail="Page not found")

    raise HTTPException(status_code=404, detail="Page not found")


@router.get("/{column_slug}/detail/{item_slug}", response_class=HTMLResponse)
async def item_detail_page(
    column_slug: str, item_slug: str, request: Request, db: Session = Depends(get_db)
):
    """Universal item detail page for products and posts"""
    column = site_service.get_column_by_slug(db, column_slug)

    if not column:
        raise HTTPException(status_code=404, detail="Page not found")

    context = get_base_context(request, db)
    context["column"] = column

    # Handle different column types
    if column.column_type == ColumnType.PRODUCT:
        product = product_service.get_product_by_slug(db, item_slug)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        context["product"] = product

        # Get related products
        if product.categories:
            context["related_products"] = product_service.get_products(
                db, category_id=product.categories[0].id, limit=4
            )

        return templates.TemplateResponse("product_detail.html", context)

    elif column.column_type == ColumnType.POST:
        post = post_service.get_post_by_slug(db, item_slug)

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        context["post"] = post

        # Get related posts
        if post.categories:
            context["related_posts"] = post_service.get_posts(
                db, category_id=post.categories[0].id, limit=3
            )

        return templates.TemplateResponse("post_detail.html", context)

    else:
        raise HTTPException(status_code=404, detail="Invalid column type for detail page")


@router.post("/contact/submit")
async def submit_contact_form(
    request: Request,
    db: Session = Depends(get_db),
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(""),
    subject: str = Form(...),
    message: str = Form(...),
):
    """
    Handle contact form submission with Pydantic validation
    """
    try:
        # Validate form data using Pydantic
        form_data = ContactFormRequest(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )

        # Create new contact message
        contact_message = ContactMessage(
            name=form_data.name,
            contact_info=f"Email: {form_data.email}"
            + (f", Phone: {form_data.phone}" if form_data.phone else ""),
            message_text=f"Subject: {form_data.subject}\n\n{form_data.message}",
            source_page_url=request.headers.get("referer", "Direct submission"),
        )

        # Save to database
        db.add(contact_message)
        db.commit()
        db.refresh(contact_message)

        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Your message has been sent successfully. We'll get back to you soon!",
                "data": {"id": contact_message.id, "name": contact_message.name},
            },
        )

    except ValidationError as e:
        # Handle Pydantic validation errors
        error_messages = []
        for error in e.errors():
            field = error["loc"][-1]
            msg = error["msg"]
            error_messages.append(f"{field}: {msg}")

        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": "Validation failed: " + "; ".join(error_messages),
            },
        )

    except Exception as e:
        db.rollback()
        logger.error(f"Error submitting contact form: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Sorry, there was an error sending your message. Please try again later.",
            },
        )
