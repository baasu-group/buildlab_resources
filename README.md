# 🚀 Internship Engineering Program

### Learn. Build. Collaborate. Ship.

Welcome to the official internship repository.

**Lead by:** [basan-ta](https://github.com/basan-ta)

This repository is designed to provide a **real-world software development experience** through a structured six-month internship program.

Instead of learning technologies in isolation, interns will work together to design, build, test, and improve a real software product.

The goal is simple:

> **Learn the fundamentals, apply them to a real project, work like a professional engineering team, and leave the internship with experience you can confidently demonstrate.**

---

#  About This Program 🌟

This is a **six-month project-based internship program** focused on practical software development.

## Program structure

The internship has two connected phases:

1. **Months 1–3 — Learning and practice:** interns build fundamentals, learn the tools for their track, complete guided exercises, practice collaboration, and receive regular reviews.
2. **Months 4–6 — Intensive real-world project work:** interns work as one product team to design, build, test, review, document, and ship the Team Management Platform.

The program is measured by learning progress, useful contributions, collaboration, quality, and the ability to explain and improve the work—not by tutorial completion alone.

Interns will work in specialized tracks while collaborating as one product team.

### Our tracks

| Track | Focus |
|---|---|
| 🎨 UI/UX Designer | Product design, UX, Figma, design systems |
| 💻 Frontend Developer | React, Next.js, Tailwind CSS |
| ⚙️ Backend Developer | Python, Django, DRF, PostgreSQL |
| 🧪 QA Engineer | Manual testing, API testing, automation mindset |

Each track has its own learning roadmap:

- [`Frontend_Resources`](./buildlab/INT-026-08-01/Frontend_Resources)
- [`Backend_resources`](./buildlab/INT-026-08-01/Backend_resources)
- [`UI_UX_resources`](./buildlab/INT-026-08-01/UI_UX_resources)
- [`QA_resources`](./buildlab/INT-026-08-01/QA_esources)

---

# What We Are Building 🎯 

The internship is centered around a **real-world Team Management Platform**.

The platform will allow users and teams to manage their daily work in one place.

### Planned features

- 🔐 User registration and authentication
- 👤 User profiles
- 👥 Team management
- 📊 Dashboard
- ✅ Task management
- 🏷️ Task status and priorities
- 🔎 Search and filtering
- 📄 Pagination
- 🔒 Role-based permissions
- 🔔 Notifications
- 📱 Responsive interface
- 🌐 REST API
- 🧪 Quality assurance and testing

The exact scope may evolve as the team learns and receives feedback.

## Learning resource hub

The website includes a central resource hub for:

- Frontend
- Backend
- UI/UX
- QA
- DevOps
- AI/ML

Each field can later contain roadmaps, documentation, practice assignments, tools, project guidance, and recommended references. Resource destinations are managed in [`buildlab/script.js`](./buildlab/script.js), so new links can be added without changing the page layout.

---

# The Philosophy

This internship is not about completing tutorials.

It is about learning how to **build software**.

You will be expected to:

> Learn → Practice → Build → Test → Review → Improve → Ship

You will make mistakes.

You will receive feedback.

You will refactor your code.

You will encounter bugs.

You will have to understand code written by someone else.

That is part of the learning process.

### We value:

- Curiosity
- Consistency
- Ownership
- Communication
- Problem solving
- Clean work
- Teamwork
- Continuous improvement

You are not expected to know everything on day one.

You are expected to **keep learning**.

---

# 🏗️ Team Structure

The project is divided into four main disciplines.

```text
                         PRODUCT
                            │
              ┌─────────────┴─────────────┐
              │                           │
           UI / UX                    Engineering
              │                           │
              │                 ┌─────────┴─────────┐
              │                 │                   │
              │             Frontend            Backend
              │                 │                   │
              └─────────────────┴─────────┬─────────┘
                                          │
                                         QA
                                          │
                                        ↓
                                        Release
```

---

# 🌐 Internship website

The static GitHub Pages site lives in [`buildlab/`](./buildlab/). The root [`index.html`](./index.html) redirects visitors there so the existing Pages URL continues working. Configure application, feedback, contact, community, and calendar links in [`buildlab/script.js`](./buildlab/script.js), then follow the [GitHub Pages setup guide](./docs/GITHUB_PAGES.md). Deployment is intentionally gated so only `basan-ta` or `baasu-group` can publish changes from `main`.

The curriculum hub is data-driven: update [`buildlab/resources/data.js`](./buildlab/resources/data.js) to add topics, official documentation, YouTube videos, search links, and real-world practice tasks for Frontend, Backend, UI/UX, QA, DevOps, and AI/ML.
