"""
Video script library for the QuickByte tech-tips Shorts channel.

IMPORTANT (do not "optimize" this into a template): YouTube's inauthentic
content policy (2026) explicitly targets videos that "look like they were
made from a template with little to no variation" or "feel interchangeable
when a viewer watches several in a row" - their own test is "if another
channel could recreate your video in an afternoon, you're in the risk zone."

Every entry below is a genuinely different FORMAT (not just different nouns
plugged into one script skeleton), each with real specific reasoning - not
generic praise or a spec sheet read aloud. New entries added later (see the
content-expansion cadence) must keep this same standard: real insight, varied
structure, and NOT every video ending in a product plug (some are pure
informational tips with no affiliate link at all - that mix matters for
looking authentic, not just for viewer trust).

Fields:
- slug: filename-safe id
- format: the structural format (for variety tracking - don't let one format dominate)
- title: on-screen hook / video title
- script: narration text for TTS (~110-170 words, ~45-65s spoken)
- footage_queries: 3-5 varied Pexels video search terms for B-roll, in order
- captions: short on-screen text overlays (NOT a transcript - sparse, punchy,
  timed to hit key beats only, since text-on-screen-as-transcript is part of
  the "no narrative" pattern YouTube flags)
- affiliate: optional {product_name, search_term} - omit entirely for pure
  informational videos (keep roughly half the library affiliate-free)
"""

SCRIPTS = [
    {
        "slug": "offload_unused_apps",
        "format": "quick_tip",
        "title": "Free up storage without deleting a single app",
        "script": (
            "Your phone storage is probably full of apps you haven't opened in months, "
            "but deleting them means losing your data and settings. There's a middle option "
            "almost nobody uses. On iPhone, go to Settings, General, iPhone Storage, and turn on "
            "Offload Unused Apps. It removes the app itself but keeps all your documents and data. "
            "The second you tap that app's icon again, it reinstalls automatically with everything "
            "still there. Android has the same idea built into Play Store settings under app archiving. "
            "I did this on a phone that was stuck at ninety-eight percent full and got back over four "
            "gigabytes in about a minute, without losing a single login or save file."
        ),
        "footage_queries": ["hand holding smartphone settings", "phone storage full screen", "scrolling app icons", "phone charging on desk"],
        "captions": ["Settings > iPhone Storage", "Offload Unused Apps", "+4GB back, zero data lost"],
    },
    {
        "slug": "fast_charging_myth",
        "format": "myth_vs_reality",
        "title": "Does fast charging actually ruin your battery?",
        "script": (
            "You've probably heard fast charging destroys your battery faster. That's mostly outdated "
            "advice. Modern phones - anything from the last four or five years - have charge controllers "
            "that manage heat and current automatically, so a genuine fast charger from the phone's own "
            "manufacturer isn't the real problem. What actually degrades batteries faster is heat. Charging "
            "in direct sunlight, charging through a thick case, or gaming while plugged in generates way "
            "more damage over time than the charging speed itself. If you want to protect your battery, "
            "the highest-leverage habit isn't avoiding fast chargers - it's taking your case off before you "
            "charge overnight and keeping the phone somewhere cool."
        ),
        "footage_queries": ["phone charging cable closeup", "phone battery icon screen", "phone on nightstand charging", "hot sunlight through window"],
        "captions": ["MYTH: fast charging kills batteries", "REALITY: heat is the real killer", "Case off + cool spot > slow charger"],
    },
    {
        "slug": "power_bank_mah_trap",
        "format": "before_you_buy",
        "title": "The number on power banks that's basically a lie",
        "script": (
            "Before you buy a power bank based on its milliamp hour rating, know that number is measured "
            "at a voltage your phone never actually uses. Power banks list capacity at three point seven "
            "volts, but your phone charges at five volts or higher, and converting between them loses energy "
            "as heat. A ten thousand milliamp hour power bank realistically gives you six to seven thousand "
            "usable milliamp hours - barely two full phone charges, not three like the box implies. The number "
            "that actually matters is the output wattage, not the capacity. A smaller battery with proper "
            "power delivery output will charge your phone faster and more efficiently than a huge one with "
            "a weak, outdated port."
        ),
        "footage_queries": ["portable power bank charging phone", "power bank specs label closeup", "person packing bag with charger", "usb c cable plugged in"],
        "captions": ["10,000mAh label", "~65% actually usable", "Watch the wattage, not the mAh"],
        "affiliate": {"product_name": "USB-C power bank with PD fast charging", "search_term": "portable charger power bank"},
    },
    {
        "slug": "browser_tab_memory",
        "format": "did_you_know",
        "title": "Your browser is quietly eating your RAM even when tabs are hidden",
        "script": (
            "If your laptop slows down with a lot of browser tabs open, most browsers now have a built-in "
            "fix you've probably never touched. It's called tab hibernation or memory saver, depending on "
            "your browser, and it automatically freezes tabs you haven't looked at in a while, releasing "
            "the memory they were using, without actually closing them. The tab reloads instantly the moment "
            "you click back to it. In Chrome it's under Settings, Performance, Memory Saver. In Edge it's "
            "Settings, System and Performance. Turning this on can free up several gigabytes of RAM on a "
            "typical browsing session with twenty or more tabs open, and most people don't even notice it "
            "happening."
        ),
        "footage_queries": ["laptop browser many tabs open", "typing on laptop keyboard", "computer settings menu screen", "laptop fan closeup"],
        "captions": ["Settings > Performance", "Memory Saver: ON", "Tabs freeze, not close"],
    },
    {
        "slug": "charging_to_100_mistake",
        "format": "common_mistake",
        "title": "Charging to 100% every single night is quietly wearing out your battery",
        "script": (
            "Keeping your phone plugged in and sitting at a full one hundred percent charge overnight is "
            "one of the most common habits that shortens battery lifespan. Lithium batteries are chemically "
            "happiest sitting between about twenty and eighty percent - full charge puts the battery under "
            "more voltage stress for hours at a time. Most modern phones actually have a setting for this now. "
            "On iPhone it's Settings, Battery, Battery Health, Optimized Battery Charging. On newer Samsung "
            "phones it's under Battery Protection. Turning it on lets the phone learn your wake-up routine and "
            "delay that last stretch of charging until right before you need it, instead of sitting at full "
            "charge for six or seven hours straight."
        ),
        "footage_queries": ["phone charging overnight bedroom", "battery percentage screen closeup", "phone on charger dark room", "person waking up checking phone"],
        "captions": ["Optimized Battery Charging", "Settings > Battery > Battery Health", "Full charge overnight = extra wear"],
    },
    {
        "slug": "back_tap_gesture",
        "format": "hidden_feature",
        "title": "The gesture built into your phone that almost nobody turns on",
        "script": (
            "There's a feature buried in accessibility settings that turns the back of your phone into an "
            "extra button. It's called Back Tap on iPhone, and there's an Android equivalent on most phones "
            "called tap gestures. You set an action for a double tap and a separate action for a triple tap "
            "on the back of the phone - things like taking a screenshot, opening the camera, or toggling "
            "flashlight. It's genuinely useful for taking a discreet screenshot without fumbling for two "
            "buttons at once. Find it on iPhone under Settings, Accessibility, Touch, Back Tap. It takes "
            "ten seconds to set up and most people who try it end up using it constantly."
        ),
        "footage_queries": ["hand holding phone back view", "tapping phone screen closeup", "phone accessibility settings menu", "person taking screenshot phone"],
        "captions": ["Settings > Accessibility > Touch", "Back Tap", "Double-tap = screenshot"],
    },
    {
        "slug": "mechanical_keyboard_budget",
        "format": "under_budget",
        "title": "You don't need a $150 keyboard to stop hating how you type",
        "script": (
            "If you spend hours a day typing and you're still on a flat laptop keyboard or a basic membrane "
            "board, the jump to a budget mechanical keyboard is one of the highest value upgrades for how a "
            "desk setup actually feels to use. You don't need the expensive hot-swappable enthusiast boards "
            "people build for fun - a solid entry-level mechanical keyboard with brown or red switches gets "
            "you most of the tactile improvement for a fraction of the price. The difference isn't really "
            "about speed, it's about fatigue - your fingers aren't bottoming out on a hard plastic membrane "
            "for eight hours straight. It's a genuinely different feeling by the end of a work day."
        ),
        "footage_queries": ["mechanical keyboard typing closeup", "desk setup keyboard mouse", "hands typing keyboard office", "keyboard switches closeup"],
        "captions": ["Membrane vs mechanical", "Less finger fatigue, not just speed", "Entry-level tactile switches = 80% of the feel"],
        "affiliate": {"product_name": "budget mechanical keyboard", "search_term": "mechanical keyboard"},
    },
    {
        "slug": "usb_c_lightning_why",
        "format": "comparison",
        "title": "Why the USB-C switch actually matters, not just for cables",
        "script": (
            "The move from Lightning to USB-C isn't just about which cable you carry. USB-C is a completely "
            "open standard, which means the port itself can support wildly different capabilities depending "
            "on the device - some support display output, some support much faster data transfer, some "
            "support way higher charging wattage. Lightning topped out around the same speed for over a "
            "decade. The tradeoff is that USB-C's flexibility means two cables that look identical can behave "
            "completely differently - one might charge fast and transfer files quickly, another might only "
            "handle slow charging. That's why the cable that came in the box matters more with USB-C than it "
            "ever did with Lightning."
        ),
        "footage_queries": ["usb c cable closeup", "charging cable comparison desk", "plugging cable into laptop", "phone charging port closeup"],
        "captions": ["Lightning: one fixed spec", "USB-C: spec varies by cable", "Same port, different capabilities"],
    },
    {
        "slug": "old_phone_security_camera",
        "format": "life_hack",
        "title": "That old phone in your drawer can replace a $60 security camera",
        "script": (
            "If you have an old phone sitting unused in a drawer, it can work as a genuinely functional home "
            "security camera instead of buying a dedicated one. Free apps like Alfred or your phone's own "
            "camera with a basic motion-detection app turn it into a live feed you can check from your current "
            "phone, with push notifications when it detects movement. Mount it on a cheap tripod or even just "
            "prop it against something facing a doorway, keep it plugged into power full time, and connect it "
            "to your wifi. The video quality on a phone from a few years ago is usually better than what "
            "budget dedicated security cameras actually offer, and it costs nothing since you already own the "
            "hardware."
        ),
        "footage_queries": ["old smartphone on shelf", "phone mounted on tripod", "home security camera app screen", "phone facing doorway"],
        "captions": ["Old phone + free app", "= live security feed", "Better camera than most $60 options"],
    },
    {
        "slug": "counterfeit_charger_red_flags",
        "format": "red_flag",
        "title": "Three signs a cheap charger is actually dangerous, not just low quality",
        "script": (
            "Not all cheap chargers are just slow - some are genuinely unsafe, and there are specific signs "
            "worth checking before you plug one in overnight. First, weight: a real fast charger has real "
            "components inside, so if it feels suspiciously light and hollow, that's a red flag. Second, "
            "check for a certification mark like UL or CE printed on it - counterfeit chargers routinely fake "
            "these, but the complete absence of any mark at all is worse. Third, if it gets noticeably hot "
            "just sitting there charging a phone at normal speed, that's a sign of poor internal regulation, "
            "which is how house fires from chargers actually happen. None of these guarantee safety on their "
            "own, but a charger that fails more than one of them isn't worth the risk for the couple dollars "
            "you'd save."
        ),
        "footage_queries": ["phone charger plugged into wall", "charging cable and adapter closeup", "wall outlet with plug", "phone charging warning concept"],
        "captions": ["Suspiciously light = red flag", "No certification mark = red flag", "Hot to the touch = red flag"],
    },
    {
        "slug": "two_factor_30_seconds",
        "format": "quick_tip",
        "title": "The 30-second setting that stops almost every account takeover",
        "script": (
            "If you've been putting off setting up two-factor authentication because it sounds like a hassle, "
            "the app-based version takes about thirty seconds per account and is genuinely worth doing today. "
            "Skip text message codes if you can - they can be intercepted through a SIM swap. Instead use an "
            "authenticator app, Google Authenticator or Authy both work fine and are free. Go into your email "
            "and banking app security settings, look for two-factor or two-step verification, and scan the QR "
            "code it shows you with the authenticator app. From then on, even if someone steals your password "
            "in a data breach, they still can't get into your account without your phone physically in hand."
        ),
        "footage_queries": ["phone authenticator app screen", "scanning qr code phone", "entering code on phone", "account security settings screen"],
        "captions": ["Skip SMS codes (SIM swap risk)", "Use an authenticator app instead", "Password leaked ≠ account taken"],
    },
    {
        "slug": "reverse_image_search_shortcut",
        "format": "hidden_feature",
        "title": "You can search using a photo instead of typing anything",
        "script": (
            "Most people don't realize you can search using an image instead of words, and it's built directly "
            "into your phone's camera and browser already. On iPhone, open a photo, tap the little sparkle "
            "icon or long-press an object in the image, and it identifies what's in it - a plant, a product, "
            "a landmark - and shows matching results. On Android it's built into Google Lens, accessible "
            "directly from the camera app or by long-pressing any image in your browser. It's genuinely useful "
            "for figuring out where to buy something you saw in a photo, identifying a plant on a walk, or "
            "translating text in a picture instantly without typing a single word."
        ),
        "footage_queries": ["phone camera scanning object", "google lens app screen", "person taking photo of plant", "phone identifying product photo"],
        "captions": ["Long-press any photo", "Or open camera > Lens", "Search with the image, not words"],
    },
    {
        "slug": "anc_earbuds_what_matters",
        "format": "before_you_buy",
        "title": "What actually separates good noise cancelling earbuds from bad ones",
        "script": (
            "Before buying noise cancelling earbuds based on the spec sheet, know that the marketing number "
            "for noise cancellation depth barely tells you anything useful. What actually matters is the seal - "
            "how well the ear tip physically blocks your ear canal - because noise cancelling electronics only "
            "handle low, steady sounds like engine hum or air conditioning. They do almost nothing for sudden "
            "sharp sounds like someone talking nearby or a door closing, and a bad physical seal makes even "
            "great electronics feel weak. That's why the same earbuds can feel amazing on one person and "
            "mediocre on another - ear shape changes the seal completely. If a company offers multiple ear tip "
            "sizes and a fit test in their app, that matters more than any noise cancellation percentage they "
            "advertise."
        ),
        "footage_queries": ["wireless earbuds case closeup", "person wearing earbuds outdoors", "earbuds ear tips comparison", "noise cancelling earbuds unboxing"],
        "captions": ["ANC spec number = mostly marketing", "The physical seal matters more", "Multiple ear tip sizes > higher dB rating"],
        "affiliate": {"product_name": "noise cancelling wireless earbuds", "search_term": "noise cancelling earbuds"},
    },
    {
        "slug": "wifi_router_placement",
        "format": "did_you_know",
        "title": "Moving your router two feet can double your wifi speed",
        "script": (
            "Where your router physically sits changes your wifi speed more than almost any setting you could "
            "change. Routers radiate signal outward and slightly downward from the antennas, so a router "
            "sitting on the floor, inside a cabinet, or behind a TV loses a huge amount of range immediately. "
            "The ideal spot is elevated, out in the open, and as central to your home as possible - a shelf in "
            "a hallway beats a closed media console every time. Mirrors and metal surfaces reflect wifi signal "
            "almost like they reflect light, and microwaves running nearby can interfere with two point four "
            "gigahertz bands specifically. Moving a router from inside a cabinet onto an open shelf a few feet "
            "away can genuinely double measured speed in the far rooms of a house."
        ),
        "footage_queries": ["wifi router on shelf", "router blinking lights closeup", "home network setup", "person checking wifi speed phone"],
        "captions": ["Router in a cabinet = signal loss", "Elevated + open + central = best", "Metal surfaces reflect wifi signal"],
    },
    {
        "slug": "laptop_screen_cleaning_mistake",
        "format": "common_mistake",
        "title": "The way most people clean their laptop screen is slowly damaging it",
        "script": (
            "Spraying glass cleaner directly onto a laptop screen or wiping it with a dry paper towel are both "
            "surprisingly common habits that damage the screen over time. Most laptop and phone screens have a "
            "thin oleophobic coating that reduces fingerprint smudging, and ammonia-based glass cleaners break "
            "that coating down with repeated use. Dry paper towels are actually abrasive at a microscopic level "
            "and create fine scratches you won't notice until the screen looks hazy under certain lighting. The "
            "safe method is a microfiber cloth, lightly dampened with plain water or a dedicated electronics "
            "cleaner, never sprayed directly onto the screen - spray it on the cloth first. It takes the same "
            "amount of time and the screen stays clear for years instead of gradually clouding."
        ),
        "footage_queries": ["cleaning laptop screen cloth", "microfiber cloth closeup", "laptop screen reflection", "person wiping phone screen"],
        "captions": ["Paper towel = micro-scratches", "Spray on cloth, never on screen", "Microfiber + water only"],
    },
]
