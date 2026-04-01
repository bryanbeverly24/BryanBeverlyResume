from flask import Flask, render_template

app = Flask(__name__)

# ── Bryan Beverly's Resume Data ───────────────────────────────────────────────
RESUME = {
    "name": "Bryan Beverly",
    "title": "Business-Oriented HR Executive",
    "tagline": "Transforming human capital into competitive advantage for Fortune 500 organizations.",
    "email": "bryanbeverly@gmail.com",
    "phone": "773.456.3328",
    "location": "Inverness, IL (Chicago)",
    "linkedin": "linkedin.com/in/bryankbeverly",
    "summary": (
        "Business-oriented HR Executive with 20+ years driving measurable performance and growth "
        "in Fortune 500 environments. Partners directly with CEOs and executive teams to transform "
        "human capital into a genuine competitive advantage delivering clear ROI through AI-powered "
        "talent strategies, accelerated leadership pipelines, and large-scale organizational change. "
        "Proven ability to build high-performing, resilient teams and cultures that execute "
        "relentlessly in complex, human-AI blended global organizations. Track record spans global "
        "corporate leadership, management consulting, entrepreneurship, and nonprofit governance."
    ),
    "experience": [
        {
            "company": "Wesco",
            "role": "Global Head of Talent, Learning, and Change",
            "period": "2021 – Present",
            "location": "Chicago",
            "context": "NYSE: WCC, Fortune #199 — $23.5B revenue, 21,000 employees, 50+ countries. Ranked #10 on Fortune's inaugural AIQ 50 list (2025).",
            "bullets": [
                "Spearheaded enterprise-wide AI Fluency Campaign, equipping thousands of employees with foundational AI skills — directly contributing to Wesco's #10 AIQ 50 ranking.",
                "Championed AI integration across HR functions: automated recruitment, modernized L&D, and optimized performance management delivering significant productivity gains and cost efficiencies.",
                "Transformed a 5-person recruitment team into a 70+ member Talent Center of Excellence spanning six specialized functions, enabling scalable, skills-based talent deployment.",
                "Directed end-to-end global talent lifecycle for 23,000 employees across 50+ countries, building a high-performance culture aligned with corporate objectives.",
                "Implemented Oracle Recruiting Cloud ATS, streamlining 2,000+ requisitions and enabling 500+ global hires monthly while substantially reducing time-to-hire and costs.",
                "Executed North America warehouse RPO program delivering 1,600 annual placements while lowering recruitment costs, turnover, and time-to-hire through data-driven optimization.",
                "Designed and launched "Leadership Essentials" program, accelerating development for 1,200 managers annually and building coaching capabilities for human-AI team leadership.",
                "Established first global performance management framework using predictive analytics, driving measurable gains in employee performance, engagement, and retention.",
            ],
        },
        {
            "company": "Human Capital Strategies and Solutions",
            "role": "Founder",
            "period": "2019 – 2021",
            "location": "Chicago",
            "context": "Boutique consultancy delivering high-impact human capital strategies to mid- and large-scale organizations.",
            "bullets": [
                "Delivered strategic consulting in talent acquisition, skills-based talent management, L&D, organizational development, performance management, and transformation.",
                "Partnered with leadership teams to design scalable people strategies that strengthened culture, leadership capability, and business performance.",
                "Created actionable frameworks that accelerated talent pipelines and built organizational agility amid digital and AI disruption.",
            ],
        },
        {
            "company": "Gallagher",
            "role": "Vice President, Global Head of Talent, Leadership & Development",
            "period": "2018 – 2019",
            "location": "Chicago",
            "context": "NYSE: AJG, Fortune #367 — $11.6B+ revenue, 56,000 employees, 30+ countries.",
            "bullets": [
                "Built cross-divisional Talent Center of Excellence integrating talent management, L&D, OD, diversity, performance management, and people analytics into a unified global strategy.",
                "Established the People Analytics function and led inaugural global attrition-prediction project in the Claims division, achieving significant turnover reduction.",
                "Created global Employee Experience framework informed by Future of Work trends, repositioning Gallagher as an employer of choice for digitally native talent.",
                "Modernized leadership development with "Leader Profile" framework and Executive Development Program, ensuring a ready-now leadership bench.",
                "Strengthened early-career pipeline through GCAP and flagship intern program, engaging 250 high-potential individuals annually.",
            ],
        },
        {
            "company": "Nielsen",
            "role": "Vice President, Global Talent Management and Transformation",
            "period": "2011 – 2018",
            "location": "Chicago",
            "context": "World's largest global data and measurement technology company — 106 countries, 44,000+ employees.",
            "bullets": [
                "Selected to lead three major business transformations delivering $50M in cost savings; earned Chairman's Award for strategic leadership.",
                "Directed global organizational redesign reducing from 7 regions to 4 market-maturity models, generating $30M in savings while improving efficiency and agility.",
                "Managed HR due diligence and integration for all M&A activity; authored HR integration playbook that maximized deal value and ensured seamless transitions.",
                "Designed comprehensive flexible talent framework encompassing performance management, D&I, succession planning, assessment, engagement, and onboarding.",
                "Served as strategic HR leader for Global Operations division as VP, Human Resources (2012–2014).",
                "Created Nielsen's first global talent management and OD strategy as Director, Global Talent Management (2011–2012).",
            ],
        },
        {
            "company": "PwC",
            "role": "Manager, Organization and People Consulting",
            "period": "2008 – 2011",
            "location": "New York City",
            "context": "Member of original core team standing up PwC's Talent Management Practice following end of non-compete with IBM.",
            "bullets": [
                "Provided operations and human capital advisory services to Fortune 500 clients.",
            ],
        },
        {
            "company": "Deloitte",
            "role": "Senior Consultant, Organization and People Consulting",
            "period": "2005 – 2008",
            "location": "Chicago",
            "context": "",
            "bullets": [
                "Provided operations and human capital advisory services to Fortune 500 clients.",
            ],
        },
        {
            "company": "Raytheon",
            "role": "HR Leadership Development Program",
            "period": "2003 – 2005",
            "location": "Boston / Tucson",
            "context": "NYSE: RTN, Fortune #55 — one of the world's largest Aerospace and Defense contractors.",
            "bullets": [
                "Completed world-class leadership development rotational program; ranked #1 for the class of 2005.",
            ],
        },
    ],
    "education": [
        {
            "school": "Loyola University Chicago",
            "degree": "M.S., Human Resource Management",
            "period": "2003",
            "detail": "Concentrations in Organizational Development and Labor Relations",
        },
        {
            "school": "University of Illinois, Champaign",
            "degree": "B.A., Psychology",
            "period": "2000",
            "detail": "Concentrations in Human Resources and Economics",
        },
    ],
    "awards": [
        "Wesco CEO Achievement Award — 2025 & 2023",
        "Nielsen Chairman's Award — 2017",
        "Elected Co-Chair, Board of Directors, The Soldiers Project (2016–2018) — nonprofit providing free mental health counseling to post-9/11 veterans and families",
    ],
}
# ──────────────────────────────────────────────────────────────────────────────


@app.route("/")
def index():
    return render_template("index.html", r=RESUME)


if __name__ == "__main__":
    app.run(debug=True)
