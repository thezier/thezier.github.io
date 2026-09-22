TITLE = "Family Sessions"
EYEBROW = "Portrait Photography &mdash; Southern California"
TAGLINE = "Connection is beautiful"
RAIL_LINE = "Family Sessions<br>Southern California"
DESCRIPTION = ("Family photography sessions in Southern California. At home, on location, or "
               "both, with a full-resolution online gallery.")
HOST = "family-portraits.mikethezier.com"
CREED_ID = "connection"
SESSIONS_KICKER = "Sessions &amp; pricing"

BRAND = "Mike Thezier Photography"
CONTACT = [
    ("tel:+19515871238", "951.587.1238"),
    ("mailto:mike@mikethezier.com", "mike@mikethezier.com"),
    ("https://mikethezier.com", "mikethezier.com"),
]

NAV = [
    ("connection", "Connection"),
    ("about", "About me"),
    ("experience", "The experience"),
    ("sessions", "Sessions &amp; pricing"),
    ("questions", "Questions"),
    ("next", "Next step"),
]

ABOUT_LEAD = "It&rsquo;s my goal to make photographs that tell your story."
EXTRA_SECTIONS = []
EXPERIENCE_FRAMES = [["g7"]]
PLACEHOLDERS = {
    "school": "Two of us and three kids, 6, 4 and 1",
    "timing": "Before the holidays, or whenever works",
}
SECTIONS = [
    ("family", "Family",
     "These are the most important people in our lives &mdash; our family (and also those who "
     "might as well be our family). I want to capture the story of who your family is, so my goal "
     "for these sessions is pretty simple: make everyone as comfortable as possible so that they "
     "can feel free to be themselves. That way, regardless whether you are all looking at the "
     "camera for a more traditional group portrait or candidly enjoying each other&rsquo;s "
     "company, we get to see the genuineness of who your family is.",
     [["heroA", "heroC", "g0", "allow-crop"]]),

    # Reworked at Mike's direction: home is the starting point, not the whole
    # answer. The job of this section is to get a family to volunteer the place
    # that already means something to them, because that is what makes the
    # photographs theirs rather than generic.
    ("locations", "Locations That Matter",
     "Home is my favorite place to photograph a family. It&rsquo;s where everyone lets their guard "
     "down &mdash; where the baby naps, where someone always sits on the same end of the couch, "
     "where you actually live. Photographs made there look like your life because they are your "
     "life.\n\n"
     "But home isn&rsquo;t the only place that holds something. The trail you walk most Saturdays. "
     "The stretch of beach you&rsquo;ve driven to every summer since the kids were born. Your "
     "grandparents&rsquo; grove. The field behind the house you&rsquo;re about to move out of. The "
     "gym, the barn, the orange tree someone planted the year your daughter was born. If a place "
     "is part of your family&rsquo;s story, it belongs in these photographs &mdash; and years from "
     "now it will be the thing that makes you stop scrolling.\n\n"
     "So tell me where your family actually spends its time and we&rsquo;ll go there. Home, "
     "somewhere that matters, or both in one session. And if nothing obvious comes to mind, "
     "that&rsquo;s completely normal &mdash; I know this area well, and I&rsquo;ll bring you "
     "options worth choosing between.",
     [["heroB", "g1", "g6"]]),

    ("legacy", "Legacy",
     "I strive to create images that will serve as a permanent reminder of the emotions, "
     "experiences, and relationships shared between you and the people who matter most to you, "
     "that can be enjoyed for years to come.",
     [["g2", "g3", "g4"]]),
]

ABOUT = [
    "My name is Mike Thezier (pronounced: tee-zee-ey) &mdash; my last name looks nothing like it "
    "sounds. I am a film and digital photographer based in Southern California. I love the "
    "outdoors, traveling, coffee, a good movie, but most of all sharing in those experiences with "
    "others.",
    "It&rsquo;s my goal to make photographs that tell your story. I enjoy working with my clients "
    "to create images that are genuine and compelling.",
]

BEATS = [
    ("Before the day", [
        "We&rsquo;ll talk before we shoot &mdash; where you want to be, what everyone is wearing, "
        "and what time of day actually works for your kids. That last one matters more than people "
        "expect. A session booked over a nap is a hard session, and I would rather move it than "
        "fight it.",
        "For clothes, my advice is the same as it is for everything else here: wear what you "
        "already own and feel like yourselves in. Pick one person&rsquo;s outfit first and build "
        "the rest around it. Neutral and natural colors photograph best, and I&rsquo;d avoid "
        "fluorescents, which reflect onto skin, and loud patterns.",
        "Bring whatever is genuinely part of your life right now. The blanket the baby will not "
        "sleep without, the dog, the truck, the instrument someone is learning. Those details are "
        "what make the photographs yours instead of generic.",
    ]),
    ("The session itself", [
        "Here is the part most parents are actually worried about, so let me answer it directly: "
        "your kids do not have to behave. They are not going to sit still, they are not going to "
        "look at the camera on command, and none of that is a problem I need you to solve for me.",
        "I don&rsquo;t line people up and count to three. We walk, we talk, I give you something "
        "to do rather than a pose to hold, and the photographs happen in between. If a toddler "
        "melts down we stop, we let it pass, and we keep going &mdash; that is a normal part of "
        "the hour, not a thing that ruined it. If someone will not look at me, I photograph them "
        "looking at you, which is usually the better frame anyway.",
        "What you get out of that is a set of photographs that look like your family actually is "
        "right now, at this age, in this season &mdash; not a version of it holding still.",
    ]),
    ("Your gallery", [
        "Your gallery lands in your inbox two to three weeks after the session. Full resolution, "
        "downloadable, yours to keep, print and share &mdash; no watermarks, no per-image fees, "
        "and no waiting on prints to find out what you got.",
        "From there you can order prints, books, albums and wall pieces straight from the gallery "
        "whenever you want them. Nothing expires on you.",
    ]),
]

TIERS = [
    dict(id="mini", name="Mini Session", hint="30 minutes", price="400",
         builtfor="Built for a family who wants one strong set of current photographs without "
                  "turning it into an event &mdash; the holiday card, a frame for the "
                  "grandparents, something for the wall.",
         includes=["Up to 30 minutes, on location or at home", "One setting",
                   "Up to 50 edited images", "Online gallery",
                   "Download of full resolution images"],
         why=None, feature=False),

    dict(id="one-hour", name="1 Hour Session", hint="1 hour", price="700",
         builtfor="Built for a family who wants room to breathe &mdash; more than one look, time "
                  "for the kids to forget the camera, and the quiet moments that only turn up "
                  "once everyone has relaxed.",
         includes=["A one hour session, on location or at home",
                   "Time for a second setting nearby",
                   "Up to 100 edited images", "Online gallery",
                   "Download of full resolution images"],
         why=("Why this over the mini.", "The first ten minutes are the awkward ones for almost "
              "everybody. A half hour spends a third of itself getting past that; an hour gets "
              "past it and then keeps going, which is where the photographs you actually frame "
              "tend to come from."),
         feature=True),

    dict(id="the-year", name="The Year", hint="2 hours &middot; with album", price="1,500",
         builtfor="Built for a family marking something specific &mdash; a new baby, a last year "
                  "at home, a move &mdash; who want the house they live in now as well as "
                  "somewhere open, and a book to hand to grandparents.",
         includes=["Up to 2 hours across two settings",
                   "Start at home, finish outside &mdash; or the other way round",
                   "Up to 200 edited images",
                   "10&times;10 lay-flat album, 20 pages",
                   "Design session &mdash; you choose the images, I lay out the book",
                   "One round of revisions before it goes to print"],
         why=("Why this over the hour.", "Two settings instead of one, and the album. In ten "
              "years the download is on a drive nobody opens; the album is the thing that stays "
              "on the shelf and gets pulled down, and it&rsquo;s the only tier where I design "
              "something for you rather than hand it over."),
         feature=False),
]

FINENOTE = ("<strong>Prints &amp; Products.</strong> Every session includes the full resolution "
            "downloads. From your gallery you&rsquo;ll have prints, books, albums and other "
            "products available at any time &mdash; The Year simply builds the album in from the "
            "start, designed with you rather than ordered on your own.")

FAQ = [
    ("What if my kids won&rsquo;t cooperate?",
     "They don&rsquo;t have to. I don&rsquo;t need anyone to sit still or look at the camera on "
     "command, and a meltdown is a normal part of an hour with small children rather than a "
     "session ruined. We stop, we let it pass, we keep going. Please don&rsquo;t spend the week "
     "before worrying about this one."),
    ("When is the best time to shoot?",
     "Usually the last couple of hours before sunset, when the light is worth having &mdash; but "
     "with young children the honest answer is whenever they are at their best. Tell me their "
     "schedule and we&rsquo;ll build around it rather than against it."),
    ("Where do we shoot?",
     "At home, somewhere outside you all enjoy, or both. Home is my favorite &mdash; it&rsquo;s "
     "where everyone lets their guard down. I&rsquo;m based in the Temecula Valley and shoot "
     "across Southern California. Orange County, San Diego and the coast are all regular trips and "
     "carry no separate travel fee at these rates."),
    ("What should we wear?",
     "Clothes you already own and feel like yourselves in. Pick one person&rsquo;s outfit first "
     "and build around it, keep to neutral and natural colors, and skip fluorescents and loud "
     "patterns. I&rsquo;ll go over it with you before the day."),
    ("How long until we see them?",
     "Your gallery arrives two to three weeks after we shoot. If you have a hard deadline &mdash; "
     "holiday cards, a grandparent&rsquo;s visit &mdash; say so when you book and I&rsquo;ll tell "
     "you honestly whether I can make it."),
]

NEXT = [
    "Pick the session that fits and send it to me with your name and roughly when you&rsquo;re "
    "hoping to shoot. I&rsquo;ll come back with dates that work.",
    "A 50% retainer holds your date and comes off the total; the balance is due on the day of your "
    "session. I&rsquo;ll send the contract and the invoice through HoneyBook, so it&rsquo;s signed "
    "and paid in one place. Until the retainer is in, the date stays open to whoever asks next.",
]

SENDNOTE = ("Nothing is booked or charged here. I&rsquo;ll come back with dates, then send your contract and invoice through HoneyBook.")

FIELDS = [
    ("name", "Your name", "", True, "name"),
    ("email", "Email", "", True, "email"),
    ("phone", "Phone", "optional", False, "tel"),
    ("school", "Who&rsquo;s in the session", "optional", False, None),
    ("timing", "When you&rsquo;re hoping to shoot", "optional", False, None),
]
