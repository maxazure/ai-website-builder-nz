#!/usr/bin/env python3
"""
为子栏目创建单页内容
"""

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.site import SiteColumn, SinglePage

# 数据库连接
DATABASE_URL = "sqlite:///instance/database.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_single_pages():
    """为SINGLE_PAGE类型的子栏目创建内容"""

    single_pages_data = [
        {
            'slug': 'school-term-dates',
            'title': '学期日期',
            'subtitle': 'Term Dates',
            'content_html': '''
                <h2>2024-2025学年学期安排</h2>

                <h3>秋季学期 Autumn Term</h3>
                <ul>
                    <li><strong>开学日期：</strong>2024年9月7日</li>
                    <li><strong>期中假期：</strong>2024年10月26日 - 11月3日</li>
                    <li><strong>学期结束：</strong>2024年12月21日</li>
                </ul>

                <h3>春季学期 Spring Term</h3>
                <ul>
                    <li><strong>开学日期：</strong>2025年1月6日</li>
                    <li><strong>期中假期：</strong>2025年2月15日 - 2月23日</li>
                    <li><strong>学期结束：</strong>2025年4月4日</li>
                </ul>

                <h3>夏季学期 Summer Term</h3>
                <ul>
                    <li><strong>开学日期：</strong>2025年4月21日</li>
                    <li><strong>期中假期：</strong>2025年5月24日 - 6月1日</li>
                    <li><strong>学期结束：</strong>2025年7月18日</li>
                </ul>

                <div class="alert alert-info mt-4">
                    <p><strong>注意事项：</strong></p>
                    <ul>
                        <li>所有课程均在周六上午进行</li>
                        <li>法定假日不上课</li>
                        <li>如遇特殊情况需要调整，学校将提前通知</li>
                    </ul>
                </div>
            ''',
            'seo_title': '学期日期 - 博文中文学校',
            'seo_description': '查看博文中文学校2024-2025学年的完整学期安排和重要日期',
        },
        {
            'slug': 'school-pta',
            'title': 'PTA家长教师协会',
            'subtitle': 'Parent-Teacher Association',
            'content_html': '''
                <h2>关于我们的PTA</h2>
                <p>博文中文学校家长教师协会（PTA）是一个由家长和教师组成的志愿组织，致力于促进家校合作，为学生创造更好的学习环境。</p>

                <h3>我们的使命</h3>
                <ul>
                    <li>促进家长与学校之间的沟通与合作</li>
                    <li>组织各类文化活动和社交活动</li>
                    <li>为学校筹集资金，改善教学设施</li>
                    <li>支持学校的教育项目和倡议</li>
                </ul>

                <h3>如何参与</h3>
                <p>我们欢迎所有家长和教师加入PTA。您可以通过以下方式参与：</p>
                <ul>
                    <li>参加每学期的PTA会议</li>
                    <li>协助组织学校活动</li>
                    <li>担任PTA委员会成员</li>
                    <li>提供您的专业技能和建议</li>
                </ul>

                <h3>联系我们</h3>
                <p>如有任何问题或建议，请通过学校邮箱 <a href="mailto:info@boweneducation.org">info@boweneducation.org</a> 联系我们，或在家长微信群中与我们互动。</p>
            ''',
            'seo_title': 'PTA家长教师协会 - 博文中文学校',
            'seo_description': '加入博文中文学校PTA，与学校携手共同促进孩子的成长和发展',
        },
        {
            'slug': 'chess-players',
            'title': '棋手信息',
            'subtitle': 'Information for Players',
            'content_html': '''
                <h2>棋手注册与认证</h2>
                <p>博文国际象棋俱乐部与英格兰国际象棋联合会（English Chess Federation, ECF）合作，为棋手提供正规的等级认证服务。</p>

                <h3>ECF会员注册</h3>
                <ul>
                    <li>所有希望参加正式比赛的棋手需要注册ECF会员</li>
                    <li>会员可以获得官方等级分（ECF Rating）</li>
                    <li>青少年会员享有优惠价格</li>
                </ul>

                <h3>等级分体系</h3>
                <p>ECF采用国际通用的等级分系统，根据比赛表现动态调整。等级分分为：</p>
                <ul>
                    <li><strong>初级：</strong>0-1000</li>
                    <li><strong>中级：</strong>1000-1600</li>
                    <li><strong>高级：</strong>1600-2000</li>
                    <li><strong>专家：</strong>2000+</li>
                </ul>

                <h3>相关链接</h3>
                <ul>
                    <li><a href="https://www.englishchess.org.uk/" target="_blank">English Chess Federation 官网</a></li>
                    <li><a href="https://www.englishchess.org.uk/ecf-membership/" target="_blank">ECF会员注册</a></li>
                    <li><a href="https://www.englishchess.org.uk/rating-lists/" target="_blank">查询等级分</a></li>
                </ul>

                <p class="mt-4"><strong>如需协助注册或有任何疑问，请联系俱乐部教练。</strong></p>
            ''',
            'seo_title': '棋手信息 - 博文国际象棋俱乐部',
            'seo_description': '了解ECF会员注册、等级分体系和相关信息',
        },
        {
            'slug': 'badminton-schedule',
            'title': '训练时间表',
            'subtitle': 'Training Schedule',
            'content_html': '''
                <h2>训练时间安排</h2>

                <h3>常规训练</h3>
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>日期</th>
                                <th>时间</th>
                                <th>级别</th>
                                <th>地点</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>每周六</td>
                                <td>10:00 - 12:00</td>
                                <td>初级班</td>
                                <td>Sale Sports Centre</td>
                            </tr>
                            <tr>
                                <td>每周六</td>
                                <td>14:00 - 16:00</td>
                                <td>中级班</td>
                                <td>Sale Sports Centre</td>
                            </tr>
                            <tr>
                                <td>每周日</td>
                                <td>10:00 - 12:00</td>
                                <td>高级班</td>
                                <td>Sale Sports Centre</td>
                            </tr>
                            <tr>
                                <td>每周日</td>
                                <td>14:00 - 17:00</td>
                                <td>竞技训练</td>
                                <td>Sale Sports Centre</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <h3>训练内容</h3>
                <ul>
                    <li><strong>初级班：</strong>基础技术教学，包括握拍、步法、基本击球</li>
                    <li><strong>中级班：</strong>技术提升，战术训练，双打配合</li>
                    <li><strong>高级班：</strong>高级技战术，体能训练，心理素质培养</li>
                    <li><strong>竞技训练：</strong>针对比赛的专项训练和实战演练</li>
                </ul>

                <h3>训练地点</h3>
                <p>
                    <strong>Sale Sports Centre</strong><br>
                    Sale Road, Sale, Manchester M33 3SL<br>
                    <a href="https://goo.gl/maps/example" target="_blank">查看地图</a>
                </p>

                <div class="alert alert-info mt-4">
                    <p><strong>注意事项：</strong></p>
                    <ul>
                        <li>请提前10分钟到场热身</li>
                        <li>自备球拍和运动装备</li>
                        <li>如遇场馆维护或特殊情况，将提前通知</li>
                    </ul>
                </div>
            ''',
            'seo_title': '训练时间表 - 博文羽毛球俱乐部',
            'seo_description': '查看博文羽毛球俱乐部的完整训练时间表和地点信息',
        },
        {
            'slug': 'programmes-haf',
            'title': 'HAF项目',
            'subtitle': 'Holiday Activities and Food Programme',
            'content_html': '''
                <h2>关于HAF项目</h2>
                <p>Holiday Activities and Food (HAF) 项目是英国政府资助的一项重要社区项目，旨在在学校假期期间为符合条件的儿童提供健康食品和有趣的活动。博文集团积极参与该项目，为当地社区的孩子们提供丰富多彩的假期活动。</p>

                <h3>项目目标</h3>
                <ul>
                    <li>为符合条件的儿童提供免费的健康餐食</li>
                    <li>组织各类教育和娱乐活动</li>
                    <li>促进儿童的身心健康发展</li>
                    <li>支持家庭减轻假期照看负担</li>
                </ul>

                <h3>活动内容</h3>
                <p>我们的HAF项目包括：</p>
                <ul>
                    <li>中华文化体验活动（书法、剪纸、中国结等）</li>
                    <li>体育运动（羽毛球、国际象棋等）</li>
                    <li>艺术创作和手工制作</li>
                    <li>团队游戏和户外活动</li>
                    <li>每日提供健康午餐和小食</li>
                </ul>

                <h3>参与资格</h3>
                <p>该项目面向5-16岁符合以下条件的儿童：</p>
                <ul>
                    <li>有资格享受免费校餐（Free School Meals）</li>
                    <li>居住在Trafford地区</li>
                </ul>

                <h3>如何报名</h3>
                <p>HAF项目通常在以下假期期间举办：</p>
                <ul>
                    <li>复活节假期（2周）</li>
                    <li>暑假（4周）</li>
                    <li>圣诞假期（1周）</li>
                </ul>
                <p>具体报名方式和时间将通过学校和社区渠道公布。如有疑问，请联系我们。</p>

                <div class="alert alert-success mt-4">
                    <p><strong>项目优势：</strong></p>
                    <ul>
                        <li>完全免费，包括所有活动和餐食</li>
                        <li>专业教练和工作人员指导</li>
                        <li>安全友好的环境</li>
                        <li>结识新朋友，学习新技能</li>
                    </ul>
                </div>
            ''',
            'seo_title': 'HAF项目 - 博文集团政府项目',
            'seo_description': '了解博文集团参与的HAF假期活动和食品项目，为儿童提供免费健康餐食和丰富活动',
        },
        {
            'slug': 'events-henan',
            'title': '河南大学合作',
            'subtitle': 'Cooperation with Henan University',
            'content_html': '''
                <h2>河南大学合作项目</h2>
                <p>博文集团与中国河南大学建立了长期战略合作伙伴关系，共同推动中英教育文化交流。</p>

                <h3>合作内容</h3>
                <ul>
                    <li><strong>师资交流：</strong>河南大学定期派遣优秀教师到英国进行文化交流和教学支持</li>
                    <li><strong>学生交流：</strong>组织学生互访活动，促进两国青少年的友谊和了解</li>
                    <li><strong>文化活动：</strong>联合举办各类中华文化推广活动和学术研讨</li>
                    <li><strong>资源共享：</strong>共享教学资源和研究成果</li>
                </ul>

                <h3>寻根之旅</h3>
                <p>作为合作项目的重要组成部分，我们每年组织"寻根之旅"活动，带领在英国长大的华裔青少年回到中国，深入了解中华文化：</p>
                <ul>
                    <li>参观河南大学校园，体验中国大学生活</li>
                    <li>游览历史文化名城，了解中国历史</li>
                    <li>与中国学生交流，建立国际友谊</li>
                    <li>参加文化体验活动（茶道、武术、传统工艺等）</li>
                </ul>

                <h3>Easter访华计划</h3>
                <p>每年复活节期间，我们组织为期两周的访华活动：</p>
                <ul>
                    <li><strong>日期：</strong>每年复活节假期</li>
                    <li><strong>对象：</strong>12-18岁学生</li>
                    <li><strong>行程：</strong>河南（开封、郑州、洛阳）+ 北京</li>
                    <li><strong>住宿：</strong>大学宿舍和精选酒店</li>
                    <li><strong>陪同：</strong>专业领队和河南大学志愿者</li>
                </ul>

                <div class="alert alert-info mt-4">
                    <p><strong>报名咨询：</strong></p>
                    <p>如对河南大学合作项目或访华活动感兴趣，请联系我们获取详细信息和报名方式。</p>
                    <p>邮箱：<a href="mailto:info@boweneducation.org">info@boweneducation.org</a></p>
                </div>
            ''',
            'seo_title': '河南大学合作 - 博文集团',
            'seo_description': '了解博文集团与河南大学的合作项目，包括寻根之旅和Easter访华计划',
        },
    ]

    for page_data in single_pages_data:
        # 获取对应的栏目
        column = session.query(SiteColumn).filter_by(slug=page_data['slug']).first()
        if not column:
            print(f"警告：找不到栏目 {page_data['slug']}")
            continue

        # 检查是否已存在
        existing = session.query(SinglePage).filter_by(column_id=column.id).first()
        if existing:
            print(f"跳过已存在的单页: {page_data['title']} ({page_data['slug']})")
            continue

        # 创建单页
        single_page = SinglePage(
            column_id=column.id,
            title=page_data['title'],
            subtitle=page_data.get('subtitle'),
            content_html=page_data['content_html'],
            seo_title=page_data.get('seo_title'),
            seo_description=page_data.get('seo_description'),
            status='published',
            published_at=datetime.now()
        )
        session.add(single_page)
        print(f"创建单页: {page_data['title']} ({page_data['slug']})")

    session.commit()
    print("\n单页内容创建完成！")

if __name__ == "__main__":
    create_single_pages()
    session.close()
