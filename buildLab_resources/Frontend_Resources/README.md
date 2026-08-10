# Frontend engineering track

## Mission

Turn approved product designs into a responsive, accessible, maintainable interface connected to the backend API. A feature is complete only when it handles real data, failures, loading, permissions, keyboard input, and smaller screens.

## Recommended stack

HTML, CSS, JavaScript, TypeScript as a later enhancement, React, Next.js, Tailwind CSS or the team’s chosen styling system, REST/JSON, Git, and Playwright for end-to-end checks.

## Six-month progression

| Month | Learn and practice | Product deliverable | Validation |
| --- | --- | --- | --- |
| 1 — Web foundations | HTML semantics, CSS layout, responsive design, JavaScript, Git, browser DevTools | Accessible static login and task-list prototype | Lighthouse/manual accessibility review; explain DOM, box model, and async basics |
| 2 — React foundations | Components, props, state, events, forms, effects, routing, API boundaries | App shell, navigation, reusable form and table primitives | Component review, keyboard test, unit tests for data transformations |
| 3 — Vertical slice | Data fetching, auth state, protected routes, error/loading states, API contract | Login plus task list/details flow connected to development API | Seeded-data demo covering happy, failure, empty, and unauthorized states |
| 4 — Feature delivery | Team management, task CRUD, search, filters, pagination, optimistic/pessimistic updates | Responsive team and task features | Pull-request review, API integration tests, visual comparison |
| 5 — Quality and performance | Accessibility, caching, performance, security basics, error reporting, test automation | Regression-tested UI and performance improvements | Lighthouse/Web Vitals evidence, Playwright critical paths, no client secrets |
| 6 — Release and handoff | Build pipeline, environment configuration, release notes, documentation, portfolio | Production-ready frontend release and case study | Reproducible build, deployment rehearsal, final demo |

## Weekly practice

- Weeks 1–4: recreate small responsive layouts and write plain JavaScript exercises.
- Weeks 5–8: build the app shell and reusable components from a design slice.
- Weeks 9–12: integrate authentication and the first API-backed task flow.
- Weeks 13–16: deliver team, role, task, search, filter, and pagination features.
- Weeks 17–20: add browser coverage, accessibility fixes, and performance evidence.
- Weeks 21–24: stabilize, document, deploy, and present the implementation.

## Required outputs

1. Semantic, responsive static exercise.
2. React app shell and component examples.
3. API client and validated response boundary.
4. Authentication and permission-aware UI.
5. Task and team features with all states.
6. Unit/component and end-to-end tests.
7. Accessibility and performance report.
8. Release notes and implementation case study.

## Frontend quality gate

- No critical console errors or broken navigation.
- Every asynchronous view has loading, empty, error, and success behavior.
- Forms have labels, validation, useful errors, and keyboard support.
- Responsive behavior is checked at mobile, tablet, and desktop widths.
- API errors are handled without leaking tokens or internal details.
- Components have one clear responsibility and avoid duplicated business rules.
- Tests cover the highest-risk user journeys, not only snapshots.

## Validated free resources

- [Frontend roadmap](https://roadmap.sh/frontend) and [React roadmap](https://roadmap.sh/react)
- [MDN Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn)
- [React Learn](https://react.dev/learn)
- [Next.js Learn](https://nextjs.org/learn)
- [Kevin Powell](https://www.youtube.com/@KevinPowell) for CSS and responsive UI
- [Traversy Media](https://www.youtube.com/@TraversyMedia) for practical projects
- [freeCodeCamp](https://www.youtube.com/@freecodecamp) for long-form fundamentals
- [HTML/CSS/JavaScript basics](https://www.udemy.com/course/curso-desarrollo-web-html-css-javascript/) — free when validated; Spanish optional supplement

See the [central resource catalog](../RESOURCE_CATALOG.md) for official documentation and replacements.

## Final assessment

A reviewer should be able to clone the project, configure documented environment variables, run checks, and complete the login-to-task flow without your help.
