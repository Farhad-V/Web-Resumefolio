# 4. Information Architecture

[UI/UX Design index](02-UI-UX-Design.md)

## Site Map and Navigation
Arrange the private workspace around Dashboard, Profile and Resumes, Files, Applications and permitted ProjectForge areas. Give employer shares a focused route scoped to the published material.

## Content Hierarchy
Show the page purpose and current resource first, followed by the main action, status and relevant secondary actions.

## Existing Design Records

## 2. Navigation and context

### Authenticated workspace

Provide consistent navigation to Presentation, Applications, Communication/Calendar, Work, Git and authorized Administration. Show the current resource and relevant context in page headings/breadcrumbs; selecting a project or repository does not extend permissions to linked resources. Keep a clear page purpose, primary next action and local secondary actions rather than placing every available operation in one undifferentiated toolbar.

Shared shell elements include current account, section navigation, resource title, main content, attributable operation feedback and contextual help. Visibility follows actual allowed discovery; do not leak private resource names through navigation, search, notifications or inaccessible link previews. A repository issue and work item may be associated without becoming one object.

### Employer experience

Use a separate minimal protected viewing route without requiring a product account. Identify permitted resume/content language and download choices only after applicable authorization. Password possession is not a verified employer identity. Unavailable/disabled/private states use safe truthful feedback; never reveal owner drafts, unrelated evidence or another-language PDF as a fallback.

### Reusable patterns

Specify consistent page headings, labeled fields, selection lists, status summaries, dialogs, tables/lists, file/variant cards and confirmation summaries. Choose an actual component library/framework and visual tokens only after compatibility/design evaluation. Status uses explicit words/icons as appropriate rather than color alone. Dense data can use a focused detail view without losing relationships or access context.

## MVP navigation and authority cues

The main dashboard leads to private Profile, Resumes/Portfolio, Cover Letters, Job Applications, My Files & Media and the authorized ProjectForge connection. Job applications is integrated core navigation; ApplyFlow is not a separate platform name. The library shows private/unselected state separately from a resume's selected/published state. Application status, next action, follow-up date and actual submitted materials remain available without email/calendar. Employer viewing requires protected resume access rather than the owner's login. Deferred mail/calendar, advanced Sprint/review/release, CI/CD and AI controls are not promised as MVP screens.
