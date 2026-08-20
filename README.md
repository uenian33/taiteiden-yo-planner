# Night of the Arts Planner — Helsinki, 20 August 2026

A time-scrubbed map of every session of **Taiteiden yö 2026**, ranked, in English,
Finnish and Chinese.

**Live: https://uenian33.github.io/taiteiden-yo-planner/**

The festival publishes ~400 events across one evening and a flat A–Z list is
useless at 19:00 when you are standing on a street corner in the rain. This turns
the programme into three things you can actually act on: *what is happening right
now near me*, *which of it is worth rearranging the evening for*, and *can I get
from this one to that one in time*.

## What it does

- **Timeline scrubber.** It opens on the time it actually is, docked as a pill in
  the corner; tap it to expand the full track, tap the clock to snap back to now.
  Drag it and the map and list follow. The band behind it
  is the hourly rain probability, the shaded half is after sunset (21:00), the
  filled area is how many events are running, and the magenta dots are the seven
  things that only exist tonight. Collapses to a pill when you want the screen back.
  Dragging it narrows the list to that minute: the three time modes are *On now*,
  *Starting soon* (the next 45 minutes) and *Rest of the night* (everything not
  finished yet), and taking hold of the track is a statement about one minute, so
  it switches to *On now* for you. Drag to 00:30 and four things are left.
- **Ranks, not favourites.** Every session is R3 (unmissable — exists tonight only
  and nothing substitutes for it), R2 (strong enough to reroute around), R1 (good
  if you are passing) or unranked. Ranks drive the marker colour and size, and each
  ranked session carries a written note explaining *why* it sits where it does.
- **Real map.** Vector basemap plus a satellite layer, light and dark.
- **My plan.** Add stops, set the arrival time for each one, and the planner works
  out the walk between them. It distinguishes a fixed performance (it ends when it
  ends) from an open-all-evening venue (elastic — you stay until you have to leave),
  and warns when a stop no longer fits. Four ready-made routes are included.
- **Two labels the flat programme hides.** *Normally closed* marks a door that is
  not usually open to the public, or not at this hour — the National Library's
  Cupola Hall, the clock tower at Central Station, an oil silo in Laajasalo.
  *Seldom seen* marks a one-off: a touring company passing through, a premiere, a
  piece performed tonight and then not again. Both are filters as well as labels.
- **Search** across event name, venue, street and description, in any language.
- **Three languages.** English, Finnish and Chinese, including the editorial notes.
  Event titles and descriptions come from the festival in Finnish and English;
  the Chinese build shows the English text with Chinese chrome and notes.
- **Practical flags** per event: booking required, limited seating, outdoors with
  tonight's rain probability, cancelled, and which sitting of a repeated piece
  this is.

## Sharing a link in a particular language

The link says which language it opens in, so you can hand a Finnish friend the
Finnish one without telling them to go and change a setting.

| Link | Opens in |
|---|---|
| `…/taiteiden-yo-planner/` | your browser's language, if it is one of the three |
| `…/taiteiden-yo-planner/en/` | English |
| `…/taiteiden-yo-planner/fi/` | Finnish |
| `…/taiteiden-yo-planner/zh/` or `…/ch/` | Chinese |
| `…/taiteiden-yo-planner/?lang=fi` | the same thing as a query, if you prefer |

A language in the link beats anything the reader chose before, so a shared link
always opens the way you sent it. Switching language in the app moves the URL
with it — a link that says `/zh/` never shows Finnish. The language directories
are real copies rather than redirects, because the point of the feature is the
link you hand somebody and a redirect rewrites that link on the way through.

**Sharing a whole evening.** *Send this evening to a friend*, at the foot of My
plan, hands the route to the phone's own share sheet where there is one and to
the clipboard where there is not — a readable list of stops plus a link carrying
the route itself: `…/zh/?plan=37917_1145,39427_1340`, each stop as session id and
arrival time. Opening it shows that evening without touching the reader's own
saved plan; the first edit they make is what adopts it.

## Design

The interface is built in **Festarri's** design language — its M3 token set, its
Roboto Flex type ramp, its light "canvas" and dark "art night" palettes, and its
bloom icon family. That family is normative in Festarri: no star, no heart and no
chevron-back anywhere, so a saved event wears the six-petal mark itself, a rank-3
pin is a single petal, and going back is the two-petal cut. Adding something to
your plan opens the bloom petal by petal — the staggered version is reserved for
the detail panel, because six staggered animations on every row of a list is the
thing that rule exists to prevent — and throws Festarri's favourite blast, ported
function for function: two rings, then waves of streaks, sparks and petals, in
the colours of whatever you just pressed. The timeline dock grows out of its own
pill rather than appearing, measured before and after and animated between.

The one colour that is not Festarri's is the rank-3 magenta, which is the colour
of the giraffes.

Opening an event is a forward move and going back is the same move reversed, so
the panel travels on one axis and the photograph settles rather than appears.
Back returns you to the view you left, at the scroll position you left it at,
with the row you opened still marked — including back into a search with its
query intact, or into the middle of a plan.

## Data

- Programme: the festival's own API, `helsinkifestival.fi/taiteidenyo/wp-json/events/v1/search`,
  fetched 20 August 2026 in both `fi` and `en`. 384 events become **423 sessions**
  because 27 of them are performed more than once and the flat listing hides that —
  Temppeliaukio has three sittings, *Landmarks* two, *TOCCATA!* two.
- Weather: [Open-Meteo](https://open-meteo.com/), hourly, for 60.17 N 24.94 E.
- Basemaps: [CARTO](https://carto.com/attributions) over OpenStreetMap, and Esri
  World Imagery for the satellite layer.
- Event photographs are served from the festival's own CDN.

The published copy quotes only a short excerpt of each official description and
links to the festival's page for the rest; `build_public.py` produces it from the
local build.

This is an **unofficial** planner and is not affiliated with the festival. The
Taiteiden yö mark identifies which festival the programme belongs to; the Festarri
mark identifies whose design language the interface is built in.

The **ranks and the notes are editorial** — one person's opinion about one evening,
not the organisers'. Times and venues come from the official listing; check it
before you set out, because programmes change on the day.

## Running it locally

```
python3 serve.py 8731     # then open http://127.0.0.1:8731
```

`index.html` is self-contained apart from the map tiles and fonts, so you can also
just open the file, or drop it on a phone.

## Layout

| | |
|---|---|
| `index.html` | the app, with the full programme text |
| `docs/index.html` | what GitHub Pages serves, descriptions excerpted |
| `build_public.py` | makes `docs/` from `index.html` |
| `serve.py` | local static server |
