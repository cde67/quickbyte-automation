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
- series: running series name ("Charging, decoded", "Before you buy", "Settings
  worth changing", "Security in 30 seconds"). Drawn under the hook; captions add
  "Part N of <series>" (series.py). A next part coming is a reason to follow.
- title: YouTube title / metadata (no longer drawn on screen)
- hook_text: the on-screen hook card in the first frame: <= 6 words, <= 34
  characters, no "!", no hype. Lead with the concrete object, price or spec
  (both breakout videos did). It complements the title, it doesn't repeat it.
  Must fit 2 lines at 84 px (caption_render.hook_layout). Falls back to title.
- hook_emph: optional word/phrase of hook_text drawn in orange (e.g. "$150")
- script: narration text for TTS (~110-170 words, ~45-65s spoken)
- footage_queries: 3-5 varied Pexels video search terms for B-roll, in order
- captions: 0-2 short key-point callouts shown as cards in the top band, timed
  to when the narration reaches them. Use {"text": ..., "at": "spoken word"}
  to pin one to an exact word; plain strings are matched automatically. (Spoken words are captioned separately,
  word-by-word, from the TTS timings - see build_video.py.)

Queue order = list order (run_cycle.py publishes the first unposted entry), so
put the scripts you most want out next earlier in the list. performance.py
records view counts per slug in performance_log.json - check it before
writing new entries and lean toward what's actually working.
- affiliate: optional {product_name, search_term} - omit entirely for pure
  informational videos (keep roughly half the library affiliate-free)
- graphics: animated explainer graphics (versus / checklist / steps / stat /
  specs), each shown when the narration reaches its `at` word - see graphics.py
  for the spec formats. At least 2 per video, together on screen >= 12 s, so
  ~40% of the runtime is original visuals. `specs` cards carry only real,
  checkable numbers (prefer ones the narration states) plus a source line.
  Text must fit the minimum font sizes: run `python3 graphics.py --check`.
- callouts (`captions`): <= 6 words each.
- footage_queries[0] is the opener: the product itself, close up (e.g. "wifi
  router closeup"), never a generic hand-holding-phone shot. Clips are never
  shared between videos (footage_ledger.json, see build_video.py).
- hashtags: 2-3 topic hashtags without '#' (description adds #shorts)
- tags: extra search tags for the upload
- question: one natural question for the description that invites comments
  (e.g. "Where is your router right now?") - not engagement bait

Style that's working (Oct 2026): ~95-110 words (~30s). End on a line that
runs straight back into the first sentence, so the Short loops seamlessly
(e.g. "...So before you blame your laptop for a slow transfer," -> "Grab two
USB-C cables from your drawer."). Read the seam as one sentence before saving it.

Tone (owner's direction): informative yet engaging, NOT corny like other tech
channels. Confident, conversational, specific. Every sentence carries a fact
or a step. Engagement comes from a sharp hook, concrete numbers and a quick
rhetorical question or two ("No rating?"), never from hype. Avoid: "insane",
"game-changer", "mind-blowing", "you won't believe", "Seriously!", filler
like "right?", and exclamation marks (zero is normal; one at most).
"""

SCRIPTS = [
    {
        "slug": "offload_unused_apps",
        "series": "Settings worth changing",
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
        "series": "Charging, decoded",
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
        "series": "Charging, decoded",
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
        "series": "Settings worth changing",
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
        "series": "Charging, decoded",
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
        "series": "Settings worth changing",
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
        "series": "Before you buy",
        "format": "under_budget",
        "title": "You don't need a $150 keyboard to stop hating how you type",
        "hook_text": "$150 keyboard? Not needed",
        "hook_emph": "$150",
        # Script upgraded Oct 16, 2026 for the Instagram re-post (title unchanged
        # so performance.py still matches the original YouTube upload).
        "script": (
            "You don't need a hundred-fifty-dollar keyboard to stop hating how you type. If you're on a flat "
            "laptop keyboard or a mushy membrane board, a budget mechanical keyboard is one of the best upgrades "
            "for your desk. Each key has its own switch, so you get a clean, consistent press instead of "
            "bottoming out on rubber. Pick brown switches for a quiet tactile bump, or red for a smooth press. "
            "Entry-level boards get you most of the feel of the enthusiast ones for a fraction of the price. "
            "The difference shows up at the end of a long day, and"
        ),
        "footage_queries": ["mechanical keyboard typing closeup", "laptop keyboard typing", "rgb mechanical keyboard", "desk setup keyboard mouse"],
        "captions": [],
        "graphics": [
            {"type": "versus", "at": "membrane", "left": ["Membrane", "mushy, bottoms out"],
             "right": ["Per-key switch", "clean, even press"], "winner": "right"},
            {"type": "checklist", "at": "brown", "title": "Pick your switch",
             "items": ["Brown: quiet tactile bump", "Red: smooth and linear"], "reveal_at": ["brown", "red"]},
        ],
        "hashtags": ["mechanicalkeyboard", "desksetup", "techtips"],
        "tags": ["budget mechanical keyboard", "best cheap keyboard", "mechanical keyboard switches"],
        "question": "What keyboard are you typing on right now?",
        "affiliate": {"product_name": "budget mechanical keyboard", "search_term": "mechanical keyboard"},
    },
    {
        "slug": "usb_c_lightning_why",
        "series": "Charging, decoded",
        "format": "comparison",
        "title": "Why the USB-C switch actually matters, not just for cables",
        "hook_text": "USB-C isn't about the cable",
        "hook_emph": "USB-C",
        # Script upgraded Oct 16, 2026 for the Instagram re-post (title unchanged).
        "script": (
            "Switching from Lightning to USB-C isn't really about which cable you carry. It's about what the port "
            "can do. Lightning ran at roughly the same speed for over a decade. USB-C is an open standard, so the "
            "same port can handle fast charging, external displays, or data transfers many times faster, "
            "depending on the device and the cable. That flexibility has a catch. Two USB-C cables can look "
            "identical and still behave completely differently, so the cable in the box matters more than it used "
            "to. Keep the fast one for your laptop and phone, because"
        ),
        "footage_queries": ["bunch of wires cables", "laptop charging", "portable ssd usb c", "usb port laptop", "phone charging"],
        "captions": [{"text": "Same plug, different cables", "at": "identical"}],
        "graphics": [
            {"type": "versus", "at": "ran", "left": ["Lightning", "one fixed speed"],
             "right": ["USB-C", "charging, video, data"], "winner": "right"},
        ],
        "hashtags": ["usbc", "iphone", "techtips"],
        "tags": ["usb c vs lightning", "usb c cable", "iphone usb c"],
        "question": "Are you fully switched to USB-C yet?",
    },
    {
        "slug": "old_phone_security_camera",
        "series": "Before you buy",
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
        "series": "Charging, decoded",
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
    # ---- Oct 2026 batch: modeled on the two breakout videos ----
    # usb_c_lightning_why (1.3K views) and mechanical_keyboard_budget (590)
    # beat everything else by 10-100x. What they share: a thing nearly
    # everyone owns, a "this vs that" or "you don't need the expensive one"
    # angle, and a concrete takeaway. Everything else (hidden settings,
    # myths, how-tos) stalled under 60 views. These stay structurally varied
    # (sequel, comparison, budget, before-you-buy, did-you-know) per the note above.
    # Each is ~35s and its last line runs back into its first (seamless loop).
    {
        "slug": "usb_c_cable_speed_test",
        "series": "Charging, decoded",
        "format": "comparison",
        "title": "Why two identical USB-C cables can charge at totally different speeds",
        "script": (
            "Grab two USB-C cables from your drawer. They look identical, but one might charge a laptop at a "
            "hundred watts while the other tops out at sixty, and one might move files dozens of times faster. "
            "Here's how to tell them apart. First, check the plug or the box for a wattage, like sixty or two "
            "hundred forty watts. Anything above sixty needs a tiny chip called an e-marker, which is why cheap "
            "cables usually stop there. Second, look for a speed rating, like twenty or forty gigabits per "
            "second. No rating? Assume it's stuck at old USB two speeds. So before you blame your laptop for a "
            "slow transfer,"
        ),
        "footage_queries": ["bunch of wires cables", "laptop charging", "portable ssd usb c", "usb port laptop", "phone charging"],
        "captions": [],
        "graphics": [
            {"type": "versus", "at": "charge", "left": ["Cable A", "100W + fast data"],
             "right": ["Cable B", "60W + USB 2 speed"]},
            {"type": "checklist", "at": "wattage", "title": "Read the label",
             "items": ["Over 60W: e-marker", "Speed: 20 or 40 Gbps", "No rating = basic cable"],
             "reveal_at": ["wattage", "speed", "no"]},
        ],
        "hashtags": ["usbc", "techtips", "charging"],
        "tags": ["usb c cable", "usb c cable speed", "e-marker", "usb c charging"],
        "question": "Do you know which of your cables is the fast one?",
        "affiliate": {"product_name": "240W USB-C cable with e-marker (USB4 40Gbps)", "search_term": "usb4 240w usb c cable"},
    },
    {
        "slug": "flagship_vs_midrange_phone",
        "series": "Before you buy",
        "format": "under_budget",
        "title": "You don't need a $1,000 phone. Here's what the expensive one actually adds",
        "hook_text": "What $1,000 phones add",
        "hook_emph": "$1,000",
        "script": (
            "You don't need a thousand-dollar phone. Here's what the expensive one actually gets you. A good "
            "mid-range phone runs the same apps, messaging and streaming just as smoothly for everyday use. What "
            "a flagship really adds comes down to three things: better photos in low light and at zoom, a faster "
            "chip that mostly matters for heavy gaming, and sometimes more years of software updates. That last "
            "one matters most. A cheaper phone with six or seven years of updates can easily outlast a pricier "
            "one. So check the update promise first, the camera second, and the chip last, because"
        ),
        "footage_queries": ["smartphone closeup", "phone camera night photo", "taking photo with smartphone",
                            "mobile gaming on phone", "smartphone screen scrolling", "phone software update screen",
                            "comparing two smartphones"],
        "captions": [],
        "graphics": [
            {"type": "versus", "at": "mid-range", "left": ["Mid-range", "same apps, just as smooth"],
             "right": ["Flagship", "camera, chip, updates"], "dur": 4.6},
            {"type": "checklist", "at": "three", "title": "What $1,000 buys",
             "items": ["Low-light + zoom photos", "Faster chip (gaming)", "More years of updates"],
             "reveal_at": ["photos", "chip", "updates"]},
            {"type": "steps", "at": "check", "title": "Check in this order",
             "items": ["Years of updates", "Camera", "Chip"], "reveal_at": ["update", "camera", "chip"]},
        ],
        "hashtags": ["smartphone", "techtips", "budgettech"],
        "tags": ["flagship vs midrange", "best budget phone", "phone buying guide"],
        "question": "Would you go mid-range for your next phone?",
    },
    {
        "slug": "esim_vs_physical_sim",
        "series": "Settings worth changing",
        "format": "comparison",
        "title": "eSIM vs a physical SIM card: what actually changes for you",
        "hook_text": "eSIM vs SIM: what changes",
        "hook_emph": "eSIM",
        "script": (
            "Your next phone might not even have a SIM tray. With an eSIM, your number "
            "lives on a chip built into the phone, not a card you can pop out. The upside: a thief can't just "
            "pull your SIM to grab your text codes, and you can add a cheap travel data plan from an app before "
            "you even land. The catch is switching phones. Instead of moving a card, you transfer the eSIM during "
            "setup or through your carrier. So before you wipe or trade in an old phone, move the eSIM first, "
            "because"
        ),
        "footage_queries": ["sim card", "smartphone settings", "traveler at airport using phone",
                            "airplane window travel", "setting up new smartphone", "hand holding two smartphones",
                            "smartphone closeup"],
        "captions": [{"text": "Cheap travel data from an app", "at": "cheap"}],
        "graphics": [
            {"type": "versus", "at": "upside", "left": ["SIM card", "easy to pull out"],
             "right": ["eSIM", "can't be pulled out"], "winner": "right", "dur": 4.3},
            {"type": "steps", "at": "catch", "title": "Switching phones",
             "items": ["Transfer during setup", "Or through your carrier", "Move it before you wipe"],
             "reveal_at": ["transfer", "carrier", "wipe"]},
        ],
        "hashtags": ["esim", "iphone", "techtips"],
        "tags": ["esim vs sim", "what is esim", "esim travel"],
        "question": "Have you switched to eSIM yet?",
    },
    {
        "slug": "tech_gifts_under_30",
        "series": "Before you buy",
        "format": "under_budget",
        "title": "Three tech gifts under $30 people actually use",
        "hook_text": "3 tech gifts under $30",
        "hook_emph": "$30",
        "script": "Three tech gifts under thirty dollars that won't end up in a drawer. First, a small thirty-watt USB-C charger. Most phones ship without one now, and it charges far faster than an old cube. Second, a long braided USB-C cable, because the one in the box never reaches the bed or the couch. Third, a tracker for their keys: an AirTag for iPhone users, or a Tile if they're on Android. Each one solves a problem they hit every day, which is the whole trick. So if you're stuck on a gift for someone who has everything, start with these",
        "footage_queries": [
            "usb c charger closeup",
            "braided usb cable",
            "phone charging on bed",
            "keys on table",
            "wrapped gifts table"
        ],
        "captions": [],
        "graphics": [
            {
                "type": "checklist",
                "at": "charger",
                "title": "Under $30",
                "items": [
                    "30W USB-C charger",
                    "Long braided cable",
                    "Key tracker"
                ],
                "reveal_at": [
                    "charger",
                    "cable",
                    "tracker"
                ],
                "hold": 1.2
            },
            {
                "type": "specs",
                "at": "solves",
                "title": "Typical prices",
                "rows": [
                    [
                        "30W charger",
                        "~$20"
                    ],
                    [
                        "Braided cable",
                        "~$12"
                    ],
                    [
                        "AirTag / Tile",
                        "~$25-29"
                    ]
                ],
                "source": "source: typical US retail, Oct 2026"
            }
        ],
        "hashtags": [
            "giftideas",
            "techgifts",
            "techtips"
        ],
        "tags": [
            "tech gifts under 30",
            "cheap tech gifts",
            "tech stocking stuffers"
        ],
        "question": "What's the most useful cheap gift you've ever gotten?",
        "affiliate": {
            "product_name": "30W USB-C PD GaN charger",
            "search_term": "30W USB-C charger"
        }
    },
    {
        "slug": "charger_brick_matters",
        "series": "Charging, decoded",
        "format": "before_you_buy",
        "title": "Your phone charges slowly because of the brick, not the cable",
        "hook_text": "Slow charging? It's the 5W brick",
        "hook_emph": "5W",
        "script": (
            "If your phone charges slowly, the brick is usually the problem, not the cable. Those old cube "
            "chargers often put out just five watts, while most modern phones can take twenty, twenty-five, or "
            "more. When you buy a new one, look for P D, short for Power Delivery, and a wattage printed right on "
            "the brick. Chargers sold as GaN pack that power into a much smaller body, and many have several "
            "ports. Just know they split their power when you plug in more than one device. For a single phone, "
            "twenty to thirty watts with P D is the sweet spot. Try one, and you'll see that"
        ),
        "footage_queries": ["charger brick", "phone charging cable", "phone charger plugged into wall",
                            "usb cable plug", "smartphone charging", "power outlet",
                            "charging station smartwatch"],
        "captions": [{"text": "Several ports share the power", "at": "split"},
                     {"text": "One phone: 20-30W with PD", "at": "single"}],
        "graphics": [
            {"type": "stat", "at": "five", "from": 5, "to": 30, "unit": "W", "label": "Old cube brick vs modern PD",
             "dur": 4.0},
            {"type": "checklist", "at": "look", "title": "Check the brick",
             "items": ["PD (Power Delivery)", "Wattage printed on it", "GaN: smaller, multi-port"],
             "reveal_at": ["p", "wattage", "gan"], "hold": 2.4},
        ],
        "hashtags": ["charging", "techtips", "iphone"],
        "tags": ["fast charger", "usb c pd charger", "gan charger", "slow charging fix"],
        "question": "What wattage is the charger on your nightstand?",
        "affiliate": {"product_name": "30W USB-C PD GaN charger", "search_term": "30w usb c gan charger"},
    },
    {
        "slug": "airtag_vs_tile_gift",
        "series": "Before you buy",
        "format": "comparison",
        "title": "AirTag or Tile? Check their phone before you buy one",
        "hook_text": "AirTag or Tile? Ask first",
        "hook_emph": "AirTag",
        "script": "An AirTag is useless as a gift for someone with an Android phone. It only sets up on an iPhone or iPad, and it finds things through Apple's Find My network, which is huge because nearly every iPhone nearby helps locate it. A Tile works with both iPhone and Android, so it's the safe pick when you don't know what phone they carry. Its network is smaller, though, so it's better for keys around the house than a bag lost across town. Android also has Google's Find Hub network, with trackers from brands like Chipolo and Pebblebee. So before you wrap a tracker, find out what phone they use, because",
        "footage_queries": [
            "airtag closeup",
            "keys on table",
            "android phone in hand",
            "backpack airport",
            "wrapping gift box"
        ],
        "captions": [],
        "graphics": [
            {
                "type": "versus",
                "at": "only",
                "left": [
                    "AirTag",
                    "iPhone only"
                ],
                "right": [
                    "Tile",
                    "iPhone + Android"
                ],
                "reveal_at": [
                    "only",
                    "both"
                ],
                "hold": 2.0
            },
            {
                "type": "checklist",
                "at": "wrap",
                "title": "Before you wrap it",
                "items": [
                    "iPhone: AirTag",
                    "Android or unsure: Tile"
                ],
                "reveal_at": [
                    "tracker",
                    "phone"
                ]
            }
        ],
        "hashtags": [
            "airtag",
            "giftideas",
            "techtips"
        ],
        "tags": [
            "airtag vs tile",
            "best tracker gift",
            "airtag for android"
        ],
        "question": "iPhone or Android in your house?",
        "affiliate": {
            "product_name": "Tile Mate bluetooth tracker",
            "search_term": "Tile Mate tracker"
        }
    },
    # ---- Oct 20, 2026 batch (weekly learn-and-write) ----
    # Old breakouts have flatlined (USB-C +3 views in 5 days); eSIM vs SIM got
    # 71 YouTube views and 186 Instagram views on day one, so a travel-eSIM
    # follow-up leads. Batch: projector two-parter, Gift of the week (photo
    # printer), 3 Kitchen tech, decoded, a keyboard sequel, holiday travel and
    # scam timing. Each carries a hook_pattern for the weekly comparison.
    {
        "slug": "travel_esim_vs_roaming",
        "series": "Settings worth changing",
        "format": "comparison",
        "hook_pattern": "price_vs",
        "title": "Travel eSIM vs your carrier's day pass: what to use abroad",
        "hook_text": "$12/day vs a travel eSIM",
        "hook_emph": "$12",
        "script": (
            "A carrier day pass for data abroad often costs ten to twelve dollars a day, so a week-long trip adds "
            "up fast. A travel eSIM is usually the cheaper route. Apps like Airalo or Holafly sell data for a "
            "country, priced by the gigabyte or by the trip, and you install it before you leave. Check two things "
            "first: your phone has to be unlocked, and it has to support eSIM, which most recent phones do. When "
            "you land, switch data to the travel eSIM and turn off roaming on your main line, or a day pass can "
            "start by accident. Then compare the total for your trip, because"
        ),
        "footage_queries": ["traveler using phone at airport", "airport terminal travelers", "tourist using phone map city",
                            "phone settings screen", "airplane landing", "smartphone closeup"],
        "captions": [{"text": "Roaming off on your main line", "at": "land"}],
        "graphics": [
            {"type": "versus", "at": "cheaper", "left": ["Day pass", "~$10-12 a day"],
             "right": ["Travel eSIM", "by the GB or trip"], "winner": "right", "dur": 4.4},
            {"type": "checklist", "at": "things", "title": "Check first",
             "items": ["Phone is unlocked", "Phone supports eSIM"], "reveal_at": ["unlocked", "support"]},
        ],
        "hashtags": ["esim", "travel", "techtips"],
        "tags": ["travel esim", "international data plan", "esim vs roaming", "airalo"],
        "question": "Where are you traveling next?",
    },
    {
        "slug": "kindle_vs_tablet_gift",
        "series": "Before you buy",
        "format": "comparison",
        "title": "Kindle or a tablet: what to get the reader on your list",
        "hook_text": "Kindle vs tablet for a reader",
        "hook_emph": "Kindle",
        "script": "A Kindle beats a tablet that costs twice as much. Its E Ink screen reflects light like paper instead of shining it at your eyes, so it's comfortable for hours and stays sharp in direct sun. One charge lasts weeks, not a day, and there are no notifications pulling them out of the book. A tablet only wins if they also want video, color comics or games. One thing to check: Kindles are built around Amazon's book store, but in the US, Libby can send free library books straight to a Kindle. So for anyone who reads more than they scroll,",
        "footage_queries": [
            "kindle e reader closeup",
            "reading ebook on couch",
            "tablet video streaming",
            "library bookshelf",
            "person reading in sunlight"
        ],
        "captions": [
            {
                "text": "No glare, even in sun",
                "at": "sun"
            }
        ],
        "graphics": [
            {
                "type": "versus",
                "at": "reflects",
                "left": [
                    "Kindle",
                    "weeks per charge"
                ],
                "right": [
                    "Tablet",
                    "charge it daily"
                ],
                "winner": "left",
                "reveal_at": [
                    "weeks",
                    "day"
                ],
                "hold": 2.0
            },
            {
                "type": "checklist",
                "at": "check",
                "title": "Before you buy",
                "items": [
                    "They mostly read",
                    "Library? Check Libby"
                ],
                "reveal_at": [
                    "kindles",
                    "libby"
                ]
            }
        ],
        "hashtags": [
            "kindle",
            "booktok",
            "giftideas"
        ],
        "tags": [
            "kindle vs ipad",
            "gift for readers",
            "is a kindle worth it"
        ],
        "question": "Paper books or e-reader?",
        "affiliate": {
            "product_name": "Kindle e-reader",
            "search_term": "Kindle Paperwhite"
        }
    },
    {
        "slug": "qi2_vs_magsafe",
        "series": "Charging, decoded",
        "format": "comparison",
        "title": "Qi2 vs MagSafe: do you need a new wireless charger?",
        "hook_text": "Qi2 is MagSafe for everyone",
        "hook_emph": "Qi2",
        "script": (
            "Qi2 is basically MagSafe made universal, and it's showing up on more and more chargers. Apple "
            "helped create it, so it uses the same kind of magnetic ring to snap your phone into the right spot. "
            "That alignment is the whole point. Old flat wireless pads waste energy as heat when your phone sits "
            "slightly off-center, which is why they charge slowly and run warm. A Qi2 charger works with recent "
            "iPhones and newer Android phones like the Pixel 10, and other phones can use it with a magnetic "
            "case. So if you're replacing an old wireless pad anyway, look for the Qi2 logo, because"
        ),
        "footage_queries": ["wireless charging phone", "wireless charging pad phone", "magnetic phone charger",
                            "smartphone on desk", "phone charging on desk", "charging station smartwatch",
                            "smartphone closeup"],
        "captions": [{"text": "Same magnetic ring as MagSafe", "at": "magnetic"},
                     {"text": "Look for the Qi2 logo", "at": "look"}],
        "graphics": [
            {"type": "versus", "at": "alignment", "left": ["Flat pad", "off-center, runs warm"],
             "right": ["Qi2", "magnets snap it into place"], "winner": "right", "dur": 6.5},
            {"type": "checklist", "at": "works", "title": "Qi2 works with",
             "items": ["Recent iPhones", "Pixel 10 + newer Android", "Others: a magnetic case"],
             "reveal_at": ["iphones", "pixel", "case"]},
        ],
        "hashtags": ["qi2", "magsafe", "techtips"],
        "tags": ["qi2 charger", "magsafe vs qi2", "wireless charging"],
        "question": "MagSafe, Qi2, or still plugging in?",
        "affiliate": {"product_name": "Qi2 magnetic wireless charger", "search_term": "qi2 magnetic charger"},
    },
    {
        "slug": "projector_lumens_spec",
        "series": "Before you buy",
        "format": "before_you_buy",
        "hook_pattern": "one_spec",
        "two_part": {"id": "projector", "part": 1},
        "title": "Cheap projector? The one spec that matters is ANSI lumens",
        "hook_text": "The 1 projector spec to check",
        "hook_emph": "1",
        "script": (
            "The one spec that matters on a cheap projector is brightness, and the number on the box often isn't "
            "the real one. Many budget projectors advertise eight or ten thousand lumens, a light-source figure "
            "that isn't what reaches the wall. Look for ANSI lumens instead, which come from a standardized test. "
            "Around two hundred ANSI lumens is fine for a small picture in a dark bedroom, while a living room "
            "with some light needs closer to five hundred or more. If a listing hides the ANSI number, assume "
            "it's low. So when a mini projector looks like a bargain, skip the giant figure and look for the word "
            "ANSI, because"
        ),
        "footage_queries": ["movie night projector screen", "home projector on table", "watching movie on projector screen",
                            "dark bedroom", "living room tv", "family movie night living room"],
        "captions": [{"text": "No ANSI number? Assume it's low", "at": "hides"}],
        "graphics": [
            {"type": "versus", "at": "advertise", "left": ["Box claim", "10,000 lumens"],
             "right": ["ANSI lumens", "standardized test"], "winner": "right",
             "reveal_at": ["advertise", "ansi"], "hold": 2.0},
            {"type": "checklist", "at": "around", "title": "ANSI lumens you need",
             "items": ["Dark bedroom: ~200", "Some light: 500+"], "reveal_at": ["dark", "living"]},
        ],
        "hashtags": ["projector", "giftideas", "techtips"],
        "tags": ["best cheap projector", "ansi lumens", "mini projector gift"],
        "question": "Bedroom, living room or backyard: where would yours go?",
    },
    {
        "slug": "projector_80_vs_300",
        "series": "Before you buy",
        "format": "comparison",
        "hook_pattern": "price_vs",
        "two_part": {"id": "projector", "part": 2},
        "title": "$80 vs $300 projector: what the extra money actually buys",
        "hook_text": "$80 vs $300 projector",
        "hook_emph": "$80",
        "script": (
            "A projector around eighty bucks that says four K usually isn't four K at all. It accepts a four K "
            "signal, but the chip inside is often only HD or full HD, so look for the word native. One closer to "
            "three hundred bucks buys three more things: brightness you can measure in ANSI lumens, "
            "streaming apps built in instead of a separate stick, and quieter fans, often with autofocus. The cheap one is fine "
            "for the occasional kids' movie. If movie night is every week, spend more, because"
        ),
        "footage_queries": ["home theater projector", "kids watching movie projector", "movie night projector screen",
                            "streaming stick tv", "kids watching movie", "living room movie night"],
        "captions": [{"text": "Look for the word native", "at": "native"}],
        "graphics": [
            {"type": "versus", "at": "accepts", "left": ["Says 4K", "accepts the signal"],
             "right": ["Native", "what you actually see"], "winner": "right", "dur": 4.2},
            {"type": "checklist", "at": "buys", "title": "What $300 adds",
             "items": ["Real ANSI lumens", "Built-in streaming apps", "Quieter, autofocus"],
             "reveal_at": ["brightness", "streaming", "quieter"]},
        ],
        "hashtags": ["projector", "movienight", "techtips"],
        "tags": ["cheap projector vs expensive", "best projector under 300", "native 1080p projector"],
        "question": "Would you spend $80 or $300 on a projector?",
    },
    {
        "slug": "budget_anc_earbuds",
        "series": "Before you buy",
        "format": "under_budget",
        "title": "You don't need $250 earbuds for good noise cancelling",
        "hook_text": "$250 earbuds? It's the seal",
        "hook_emph": "$250",
        "script": (
            "You don't need two-hundred-fifty-dollar earbuds for good noise cancelling. Here's what actually "
            "blocks the noise. The noise cancelling chip handles low, steady sounds like engine hum or an air "
            "conditioner, but it barely touches voices or a door slamming. What blocks those is the seal: how "
            "well the ear tip plugs your ear. That's why an under-a-hundred-dollar pair with the right fit can get "
            "surprisingly close to a flagship. The expensive pairs mostly add better call quality and app "
            "features. So before you upgrade, try every tip size in the box and run the fit test if your app has "
            "one, because"
        ),
        "footage_queries": ["wireless earbuds", "wireless earbuds case closeup", "air conditioner",
                            "door closing", "airplane cabin passengers", "person putting in earbuds",
                            "person wearing earbuds commuting"],
        "captions": [{"text": "Right fit: close to a flagship", "at": "fit"},
                     {"text": "Pricier pairs add calls + app features", "at": "expensive"}],
        "graphics": [
            {"type": "versus", "at": "chip", "left": ["ANC chip", "blocks engine hum, AC"],
             "right": ["Ear tip seal", "blocks voices, slams"], "reveal_at": ["chip", "seal"], "hold": 2.2},
            {"type": "checklist", "at": "upgrade", "title": "Before you upgrade",
             "items": ["Try every tip size", "Run the fit test"], "reveal_at": ["tip", "fit"]},
        ],
        "hashtags": ["earbuds", "airpods", "techtips"],
        "tags": ["best budget earbuds", "noise cancelling earbuds", "airpods pro alternative"],
        "question": "What earbuds are you using right now?",
        "affiliate": {"product_name": "noise cancelling wireless earbuds", "search_term": "noise cancelling earbuds"},
    },
    {
        "slug": "photo_printer_gift_of_week",
        "series": "Gift of the week",
        "format": "gift_pick",
        "hook_pattern": "look_identical",
        "title": "Mini photo printer gift: Zink or dye? Check the paper first",
        "hook_text": "Same printer? Different prints",
        "hook_emph": "prints",
        "script": (
            "Two mini photo printers can look almost the same and make completely different prints. Zink printers, "
            "like the Kodak Step, use paper with the color built in, so there's no ink at all. You get two by "
            "three inch sticky-back prints in under a minute, which kids and teens love for journals, lockers and "
            "phone cases. Printers that use dye cartridges make bigger prints that look more like real photos, "
            "with a protective coat on top. So for the scrapbooker or the teenager, a Zink printer is the fun "
            "gift. For someone who frames photos, go with dye. Ask which they'd use, because"
        ),
        "footage_queries": ["printing photos", "polaroid photos on table", "teenager decorating journal",
                            "photo album", "framed photos on wall", "wrapping gift box"],
        "captions": [{"text": "Prints in under a minute", "at": "minute"}],
        "graphics": [
            {"type": "versus", "at": "zink", "left": ["Zink", "sticky-back, no ink"],
             "right": ["Dye cartridge", "photo look, coated"], "reveal_at": ["zink", "dye"], "hold": 2.0},
            {"type": "checklist", "at": "scrapbooker", "title": "Who it's for",
             "items": ["Journals, lockers: Zink", "Framed photos: dye"], "reveal_at": ["scrapbooker", "frames"]},
        ],
        "hashtags": ["giftideas", "photoprinter", "techgifts"],
        "tags": ["mini photo printer", "kodak step printer", "gifts for teens", "photo printer gift"],
        "question": "Who on your list would actually use a photo printer?",
        "affiliate": {"product_name": "Kodak Step instant photo printer (Zink)", "search_term": "kodak step photo printer"},
    },
    {
        "slug": "instant_read_thermometer",
        "series": "Kitchen tech, decoded",
        "format": "under_budget",
        "hook_pattern": "price_vs",
        "title": "Instant-read thermometer: the $20 one does most of the job",
        "hook_text": "$20 vs $100 thermometer",
        "hook_emph": "$20",
        "script": (
            "A twenty-dollar instant-read thermometer does most of what a hundred-dollar one does. At the top end "
            "you're paying for speed and precision: premium models read in about a second and are accurate to "
            "within about half a degree. Budget ones, like the ThermoPro TP19H, take a few seconds at most, which "
            "is plenty for chicken, steak or a holiday turkey. Check three things: a probe long enough to reach "
            "the center of a roast, a backlit screen for grilling after dark, and a waterproof rating so it "
            "survives the sink. Then cook to temperature, not time, since"
        ),
        "footage_queries": ["grilling steak", "cooking steak pan", "roast chicken oven",
                            "grilling at night", "washing dishes sink", "thanksgiving turkey"],
        "captions": [{"text": "Cook to temperature, not time", "at": "temperature"}],
        "graphics": [
            {"type": "versus", "at": "paying", "left": ["$100 model", "1-second reads"],
             "right": ["~$20 model", "a few seconds"], "dur": 4.2},
            {"type": "checklist", "at": "three", "title": "Check these",
             "items": ["Probe reaches the center", "Backlit screen", "Waterproof"],
             "reveal_at": ["probe", "backlit", "waterproof"]},
        ],
        "hashtags": ["kitchengadgets", "cooking", "techtips"],
        "tags": ["instant read thermometer", "best meat thermometer", "thermopro tp19h", "gifts for dad"],
        "question": "Do you cook by time or by temperature?",
        "affiliate": {"product_name": "instant-read meat thermometer", "search_term": "instant read meat thermometer"},
    },
    {
        "slug": "wifi7_vs_wifi6_router",
        "series": "Before you buy",
        "format": "comparison",
        "title": "Wi-Fi 7 vs Wi-Fi 6: do you actually need the new router?",
        "hook_text": "Wi-Fi 7 router? Check your plan",
        "hook_emph": "Wi-Fi 7",
        "script": (
            "A new Wi-Fi 7 router probably won't make your internet any faster. Your wifi can only be "
            "as fast as the plan coming into your house. If you're paying for three hundred megabits, a decent "
            "Wi-Fi 6 router already delivers that, so Wi-Fi 7's multi-gig speeds just go unused. It also only "
            "helps devices that support it, which is still mostly the newest phones and laptops. Where it does "
            "help is a home packed with devices, or a multi-gig fiber plan. So before you upgrade, run a speed "
            "test right next to your router, because unless you're on multi-gig fiber,"
        ),
        "footage_queries": ["router closeup", "internet speed test on phone", "family using devices at home",
                            "laptop on couch at home", "smartphone and laptop on desk", "fiber optic cable closeup",
                            "wifi network laptop"],
        "captions": [{"text": "Speed test next to the router", "at": "test"}],
        "graphics": [
            # 9.6 / 46 Gbps: peak PHY rates in the IEEE 802.11ax (Wi-Fi 6) and
            # 802.11be (Wi-Fi 7) standards; 300 Mbps is the plan in the narration.
            {"type": "specs", "at": "three", "title": "Your plan vs the router",
             "rows": [["Your plan", "300 Mbps"], ["Wi-Fi 6 peak", "9.6 Gbps"], ["Wi-Fi 7 peak", "46 Gbps"]],
             "highlight": 0, "reveal_at": ["three", "6", "multi"],
             "source": "Peak rates: IEEE 802.11ax / 802.11be"},
            {"type": "checklist", "at": "helps", "title": "Wi-Fi 7 only helps",
             "items": ["Devices that support it", "Device-packed homes", "Multi-gig fiber plans"],
             "reveal_at": ["support", "packed", "fiber"]},
        ],
        "hashtags": ["wifi", "techtips", "router"],
        "tags": ["wifi 7 vs wifi 6", "do i need wifi 7", "slow wifi fix"],
        "question": "What speed do you actually get next to your router?",
    },
    {
        "slug": "streaming_stick_gift",
        "series": "Before you buy",
        "format": "before_you_buy",
        "title": "Before you gift a streaming stick, check their TV",
        "hook_text": "Streaming stick? Check TV",
        "hook_emph": "TV",
        "script": "A streaming stick can be a pointless gift if their TV is already smart. But it's one of the best upgrades for an older TV, or a smart TV whose built-in apps have gotten slow. Before you buy, check two things. First, the ports: it needs a free HDMI port, and most also need power from the TV's USB port or a wall outlet. Second, resolution: if the TV is 4K, get a 4K stick, otherwise the cheaper HD model looks the same. Roku, Fire TV and Google TV all have the big apps, so pick the one that matches their phone or smart speaker, because",
        "footage_queries": [
            "streaming stick hdmi",
            "tv remote living room",
            "hdmi port back of tv",
            "4k tv living room",
            "family watching tv"
        ],
        "captions": [
            {
                "text": "Match their phone or speaker",
                "at": "matches"
            }
        ],
        "graphics": [
            {
                "type": "checklist",
                "at": "upgrades",
                "title": "Worth it for",
                "items": [
                    "TVs with no smart apps",
                    "Smart TVs gone slow"
                ],
                "reveal_at": [
                    "older",
                    "slow"
                ]
            },
            {
                "type": "checklist",
                "at": "check",
                "title": "Check the TV",
                "items": [
                    "Free HDMI port",
                    "4K TV? Get a 4K stick"
                ],
                "reveal_at": [
                    "ports",
                    "resolution"
                ]
            }
        ],
        "hashtags": [
            "streaming",
            "giftideas",
            "techtips"
        ],
        "tags": [
            "best streaming stick gift",
            "roku vs fire tv stick",
            "do i need a streaming stick"
        ],
        "question": "Is your TV's built-in app menu slow too?",
        "affiliate": {
            "product_name": "4K streaming stick",
            "search_term": "4K streaming stick"
        }
    },
    {
        "slug": "ssd_old_laptop_upgrade",
        "series": "Before you buy",
        "format": "under_budget",
        "title": "Don't replace your slow old laptop until you check this one part",
        "hook_text": "Slow laptop? Swap in an SSD",
        "hook_emph": "SSD",
        "script": (
            "Don't replace your slow old laptop until you check this one part. If it's five or more years old and "
            "takes forever to boot, the culprit is often a spinning hard drive, not the processor. Swapping in a "
            "solid-state drive costs far less than a new laptop and cuts boot times from minutes to seconds. But check "
            "two things first. Does your laptop have a replaceable drive? Most older Windows laptops do, but "
            "newer MacBooks don't. And which type does it take: a two-and-a-half-inch SATA drive, or a small M "
            "dot two stick? Search your model number plus SSD upgrade, and"
        ),
        "footage_queries": ["hard drive closeup", "old laptop on desk", "frustrated person waiting at laptop",
                            "computer repair technician", "laptop motherboard", "opening laptop back panel",
                            "person typing on laptop happy"],
        "captions": [{"text": "Spinning hard drive = slow boot", "at": "spinning"}],
        "graphics": [
            {"type": "versus", "at": "swapping", "left": ["Hard drive", "boots in minutes"],
             "right": ["SSD", "boots in seconds"], "winner": "right", "dur": 5.6},
            {"type": "checklist", "at": "check", "title": "Before you buy",
             "items": ["Replaceable drive?", "SATA 2.5\" or M.2?", "Search: model + SSD"],
             "reveal_at": ["replaceable", "sata", "search"]},
        ],
        "hashtags": ["laptop", "pcupgrade", "techtips"],
        "tags": ["ssd upgrade", "slow laptop fix", "hdd to ssd"],
        "question": "How old is the laptop you're using right now?",
        "affiliate": {"product_name": "2.5 inch SATA SSD 500GB", "search_term": "2.5 inch sata ssd 500gb"},
    },
    # ---- Oct 2026, batch 2: the five older scripts re-angled into the formats
    # that win (head-to-head choices / "you don't need the expensive one"),
    # plus one timely topic (Qi2 chargers are replacing MagSafe-only pads).
    {
        "slug": "smart_speaker_gift",
        "series": "Before you buy",
        "format": "comparison",
        "title": "Echo or Nest? Pick the smart speaker that fits their home",
        "hook_text": "Echo or Nest gift?",
        "hook_emph": "Echo",
        "script": "The best smart speaker gift is whichever one matches the stuff they already own. An Echo runs Alexa and fits homes that use Amazon, like Prime Music, a Ring doorbell or a Fire TV. A Nest speaker runs Google's assistant and fits homes with Android phones, Google TV or Nest cameras. If they have an iPhone and Apple Music, a HomePod mini is the one that really works with it, though it costs more. Most smart plugs and bulbs work with Alexa and Google, so either one can run their lights. So before you pick by price, look at their phone and their TV, because",
        "footage_queries": [
            "smart speaker closeup",
            "amazon echo speaker",
            "google nest speaker",
            "smart home living room",
            "video doorbell"
        ],
        "captions": [
            {
                "text": "iPhone home? HomePod mini",
                "at": "homepod"
            }
        ],
        "graphics": [
            {
                "type": "versus",
                "at": "echo",
                "left": [
                    "Echo",
                    "Amazon homes"
                ],
                "right": [
                    "Nest",
                    "Google homes"
                ],
                "reveal_at": [
                    "echo",
                    "nest"
                ],
                "hold": 2.0
            },
            {
                "type": "checklist",
                "at": "pick",
                "title": "Look at their",
                "items": [
                    "Phone",
                    "TV"
                ],
                "reveal_at": [
                    "phone",
                    "tv"
                ]
            }
        ],
        "hashtags": [
            "smarthome",
            "giftideas",
            "alexa"
        ],
        "tags": [
            "echo vs google nest",
            "best smart speaker gift",
            "alexa vs google home"
        ],
        "question": "Alexa, Google, or neither in your house?",
        "affiliate": {
            "product_name": "smart speaker",
            "search_term": "Echo Pop smart speaker"
        }
    },
    {
        "slug": "burr_vs_blade_grinder",
        "series": "Kitchen tech, decoded",
        "format": "comparison",
        "hook_pattern": "price_vs",
        "title": "Blade vs burr coffee grinder: why the $20 one tastes bitter",
        "hook_text": "$20 grinder, bitter coffee",
        "hook_emph": "$20",
        "script": (
            "A twenty-dollar blade grinder can make good beans taste bitter and sour in the same cup. The blade "
            "chops at random, so you get dust next to big chunks. The dust over-extracts and turns bitter, while "
            "the chunks under-extract and taste sour. A burr grinder crushes beans between two plates set a fixed "
            "distance apart, so the pieces come out about the same size. That consistency often matters more than "
            "the coffee maker. Entry-level burr grinders, like the Baratza Encore, have forty settings, from fine "
            "for pour-over to coarse for French press. Before you buy a new coffee maker, upgrade the grinder, "
            "because"
        ),
        "footage_queries": ["coffee grinder", "coffee beans closeup", "ground coffee",
                            "pour over coffee", "french press coffee", "coffee maker kitchen"],
        "captions": [{"text": "Upgrade the grinder first", "at": "upgrade"}],
        "graphics": [
            {"type": "checklist", "at": "dust", "title": "Uneven grind", "style": "avoid",
             "items": ["Dust: bitter", "Chunks: sour"], "reveal_at": ["dust", "chunks"]},
            {"type": "versus", "at": "crushes", "left": ["Blade", "random chop"],
             "right": ["Burr", "even size"], "winner": "right", "dur": 4.4},
        ],
        "hashtags": ["coffee", "kitchengadgets", "techtips"],
        "tags": ["burr vs blade grinder", "best coffee grinder", "baratza encore"],
        "question": "Blade, burr or pre-ground in your kitchen?",
        "affiliate": {"product_name": "conical burr coffee grinder", "search_term": "burr coffee grinder"},
    },
    {
        "slug": "keyboard_gift_size",
        "series": "Before you buy",
        "format": "before_you_buy",
        "hook_pattern": "dont_until",
        "title": "Gifting a mechanical keyboard? Check the size before the switches",
        "hook_text": "Don't gift a keyboard yet",
        "hook_emph": "keyboard",
        "script": (
            "Don't gift a mechanical keyboard until you know whether they use a number pad. Full-size boards have "
            "one, which matters for spreadsheets and data entry. Tenkeyless boards drop it, so the mouse sits "
            "closer and the desk feels bigger. Seventy-five percent boards go smaller still but keep the arrows "
            "and the function row, which makes them a safe pick for most gamers and writers. Then think about "
            "noise. If they share a room or take calls, choose red or brown switches over clicky blue ones. "
            "Budget tenkeyless boards like the Redragon K552 cost far less than enthusiast models. So it's simple:"
        ),
        "footage_queries": ["mechanical keyboard typing closeup", "spreadsheet on computer screen",
                            "gaming setup keyboard mouse", "person writing on laptop", "video call at desk",
                            "wrapped gift box"],
        "captions": [],
        "graphics": [
            {"type": "checklist", "at": "spreadsheets", "title": "Pick the size",
             "items": ["Full: number pad", "Tenkeyless: no numpad", "75%: keeps the arrows"],
             "reveal_at": ["spreadsheets", "tenkeyless", "percent"]},
            {"type": "versus", "at": "noise", "left": ["Blue switches", "clicky, loud"],
             "right": ["Red or brown", "quieter"], "winner": "right", "dur": 4.0},
        ],
        "hashtags": ["mechanicalkeyboard", "giftideas", "desksetup"],
        "tags": ["mechanical keyboard gift", "tenkeyless vs full size", "gifts for gamers"],
        "question": "Number pad or no number pad?",
        "affiliate": {"product_name": "budget mechanical keyboard", "search_term": "mechanical keyboard"},
    },
    {
        "slug": "sms_codes_vs_authenticator",
        "series": "Security in 30 seconds",
        "format": "comparison",
        "title": "Text codes vs an authenticator app: which one actually protects you?",
        "hook_text": "Text codes: the weakest 2FA",
        "hook_emph": "Text codes",
        "script": (
            "Text message codes are better than nothing, but they're the weakest kind of two-factor. "
            "A scammer can talk your carrier into moving your number to their SIM card, and then your codes go "
            "straight to them. An authenticator app creates the codes on your phone itself, so there's nothing to "
            "intercept. Setting one up takes about thirty seconds per account. Install a free authenticator app, "
            "open your account's security settings, choose authenticator app, and scan the QR code. Start with "
            "your email and your bank, because"
        ),
        "footage_queries": ["text message", "text message on phone closeup", "phone text message notification",
                            "hacker typing laptop dark", "scanning qr code phone", "smartphone security",
                            "person banking on phone"],
        "captions": [{"text": "About 30 seconds per account", "at": "setting"}],
        "graphics": [
            {"type": "versus", "at": "scammer", "left": ["Text codes", "can be redirected"],
             "right": ["App codes", "made on your phone"], "winner": "right",
             "reveal_at": ["scammer", "authenticator"], "hold": 2.6},
            {"type": "steps", "at": "install", "items": ["Install the app", "Open security settings",
                                                         "Choose authenticator", "Scan the QR code"],
             "reveal_at": ["install", "security", "choose", "scan"]},
        ],
        "hashtags": ["cybersecurity", "2fa", "techtips"],
        "tags": ["two factor authentication", "sim swap", "authenticator app"],
        "question": "Are you still using text codes anywhere?",
    },
    # ---- Nov 5 2026 weekly batch + reorder: kitchen and "don't replace until" lead (thermometer,
    # grinder, SSD-laptop broke out), gift budgets/Gift of the week mid-queue, Black Friday deal-literacy
    # timed for ~Nov 14-17, weakest formats (settings/hidden-feature style) moved to the back.
    {
        "slug": "smart_ring_vs_watch_gift",
        "series": "Before you buy",
        "format": "comparison",
        "hook_pattern": "one_spec",
        "title": "Smart ring vs smartwatch gift: check the monthly fee first",
        "hook_text": "Smart ring gift? Check the fee",
        "hook_emph": "fee",
        "script": (
            "Some smart rings keep charging you after you buy them. The Oura Ring needs a membership, about six "
            "dollars a month, for most of its insights. Samsung's Galaxy Ring has no subscription, but it only "
            "works with Android phones. What a ring does well is sleep tracking, since it's comfortable at night "
            "and the battery lasts most of a week. What it can't do is show texts or take calls, because there's "
            "no screen. So for someone who wants notifications, get a watch. For better sleep data, a ring makes "
            "sense. Just remember that"
        ),
        "footage_queries": ["smartwatch on wrist", "sleeping in bed", "person sleeping at night",
                            "checking smartwatch notification", "person running with smartwatch", "phone health app"],
        "captions": [{"text": "No screen: no texts or calls", "at": "screen"}],
        "graphics": [
            {"type": "versus", "at": "membership", "left": ["Oura", "~$6 a month"],
             "right": ["Galaxy Ring", "no fee, Android only"], "reveal_at": ["membership", "subscription"],
             "hold": 1.8},
            {"type": "checklist", "at": "sleep", "title": "Ring or watch?",
             "items": ["Ring: sleep tracking", "Watch: texts and calls"], "reveal_at": ["sleep", "notifications"]},
        ],
        "hashtags": ["smartring", "giftideas", "techtips"],
        "tags": ["smart ring", "oura vs galaxy ring", "smart ring vs smartwatch"],
        "question": "Would you wear a ring to bed for sleep data?",
    },
    {
        "slug": "air_fryer_size_check",
        "series": "Kitchen tech, decoded",
        "format": "before_you_buy",
        "hook_pattern": "one_spec",
        "title": "Before you buy an air fryer, check the quarts, not the presets",
        "hook_text": "Air fryer? Check the quarts",
        "hook_emph": "quarts",
        "script": (
            "The number that matters on an air fryer is the basket size in quarts. A two-quart model handles fries "
            "for one person. Three to four quarts fits two people, and a family of four usually needs five quarts "
            "or more, because food only crisps in a single layer. Pile it up and the middle steams instead. The "
            "presets matter far less, since most of them are just a temperature and a timer you could set "
            "yourself. A five-quart basket, like the Cosori Pro LE, covers most households. So if you're shopping "
            "for one this season, remember that"
        ),
        "footage_queries": ["crispy chicken wings", "family dinner table", "kitchen countertop appliances",
                            "cooking at home kitchen", "french fries on plate", "kitchen timer"],
        "captions": [{"text": "Single layer = crispy", "at": "layer"}],
        "graphics": [
            {"type": "specs", "at": "handles", "title": "Basket size",
             "rows": [["1 person", "2 qt"], ["2 people", "3-4 qt"], ["Family of 4", "5 qt+"]],
             "reveal_at": ["person", "people", "family"], "source": "typical sizing guidance"},
            {"type": "versus", "at": "presets", "left": ["Presets", "a temp + a timer"],
             "right": ["Basket size", "what matters"], "winner": "right", "dur": 4.0},
        ],
        "hashtags": ["airfryer", "kitchengadgets", "techtips"],
        "tags": ["best air fryer", "air fryer size guide", "air fryer for family"],
        "question": "How many people does your air fryer cook for?",
        "affiliate": {"product_name": "5-quart basket air fryer", "search_term": "5 quart air fryer"},
    },
    {
        "slug": "move_router_before_upgrading",
        "series": "Before you buy",
        "format": "before_you_buy",
        "title": "Don't buy a new router until you try moving this one",
        "hook_text": "Router on the floor? Move it",
        "hook_emph": "floor",
        "script": (
            "Don't buy a new router until you try moving the one you have. Where it sits can matter more than "
            "which model it is. A router sends its signal outward in every direction, so one on the floor, inside "
            "a cabinet or behind the TV loses range right away. Put it up high, out in the open and as central as "
            "you can. Keep it away from mirrors and big metal objects, which reflect the signal, and from the "
            "microwave, which interferes with the two point four gigahertz band. Then run a speed test in your "
            "slowest room. If it's still slow, upgrade. But"
        ),
        "footage_queries": ["router", "tv cabinet living room", "hallway shelf home",
                            "person using phone on couch", "mirror in living room", "microwave oven closeup",
                            "internet speed test on phone"],
        "captions": [{"text": "Placement can matter more", "at": "matter"},
                     {"text": "Speed test in your slowest room", "at": "run"}],
        "graphics": [
            {"type": "versus", "at": "floor", "left": ["Floor or cabinet", "loses range right away"],
             "right": ["Up high", "open and central"], "winner": "right",
             "reveal_at": ["floor", "high"], "hold": 2.4},
            {"type": "checklist", "at": "keep", "title": "Keep it away from", "style": "avoid",
             "items": ["Mirrors", "Big metal objects", "Microwaves (2.4 GHz)"],
             "reveal_at": ["mirrors", "metal", "microwave"], "hold": 3.2},
        ],
        "hashtags": ["wifi", "router", "techtips"],
        "tags": ["slow wifi fix", "router placement", "wifi tips"],
        "question": "Where is your router right now?",
    },
    {
        "slug": "photo_frame_grandparents_gift",
        "series": "Before you buy",
        "format": "life_hack",
        "title": "The tech gift grandparents actually use every day",
        "hook_text": "Grandparents use this daily",
        "hook_emph": "daily",
        "script": "A Wi-Fi photo frame is the tech gift grandparents actually use every day. The family sends photos from their phones through an app, and they just show up on the frame, so there's nothing for grandma or grandpa to learn. Two things to check before you buy. Does it need a monthly subscription for storage or features? Some do, some don't. And set it up yourself before you give it, on their Wi-Fi if you can, so it works the moment they plug it in. Then add the first few photos, because",
        "footage_queries": [
            "digital photo frame",
            "grandmother smiling",
            "family taking photo smartphone",
            "elderly couple living room",
            "wrapped gift"
        ],
        "captions": [
            {
                "text": "Nothing new to learn",
                "at": "learn"
            }
        ],
        "graphics": [
            {
                "type": "steps",
                "at": "sends",
                "title": "How it works",
                "items": [
                    "Family sends photos",
                    "They appear on the frame"
                ],
                "reveal_at": [
                    "sends",
                    "show"
                ]
            },
            {
                "type": "checklist",
                "at": "check",
                "title": "Before you buy",
                "items": [
                    "Subscription required?",
                    "Set it up first"
                ],
                "reveal_at": [
                    "subscription",
                    "yourself"
                ]
            }
        ],
        "hashtags": [
            "giftideas",
            "grandparents",
            "techtips"
        ],
        "tags": [
            "gift for grandparents",
            "digital photo frame gift",
            "wifi photo frame"
        ],
        "question": "Who on your list would love this?",
        "affiliate": {
            "product_name": "WiFi digital photo frame",
            "search_term": "WiFi digital photo frame"
        }
    },
    {   'slug': 'phone_battery_before_upgrade',
        'series': 'Before you buy',
        'format': 'under_budget',
        'hook_pattern': 'dont_until',
        'title': "Don't replace your phone until you check its battery health",
        'hook_text': 'Check battery before upgrading',
        'hook_emph': 'battery',
        'script': "Don't replace your phone until you check one number: battery health. On iPhone, it's in "
                  'Settings, Battery, Battery Health. Below eighty percent, Apple considers the battery worn, '
                  'and a worn battery can slow the phone down and leave it dead by mid-afternoon. A replacement '
                  'at Apple usually costs around a hundred dollars, a fraction of a new phone. On newer Pixels, '
                  'look under Settings, Battery. On Samsung, run the battery test in the Samsung Members app. If '
                  'the health is fine and the phone still lags, then upgrading makes sense. So before you head '
                  'to the store,',
        'footage_queries': [   'phone charging',
                               'person using smartphone',
                               'smartphone settings screen',
                               'phone repair',
                               'person holding iphone',
                               'phone store'],
        'captions': [{'text': 'Samsung: Members app', 'at': 'samsung'}],
        'graphics': [   {   'type': 'stat',
                            'at': 'eighty',
                            'from': 100,
                            'to': 80,
                            'unit': '%',
                            'label': 'battery health: worn below this'},
                        {   'type': 'versus',
                            'at': 'replacement',
                            'left': ['New battery', 'about $100'],
                            'right': ['New phone', '$800+'],
                            'winner': 'left',
                            'reveal_at': ['replacement', 'fraction'],
                            'hold': 1.6}],
        'hashtags': ['iphone', 'battery', 'techtips'],
        'tags': ['should i upgrade my phone', 'phone battery health', 'iphone battery replacement'],
        'question': "What's your battery health at right now?"},
    {   'slug': 'electric_kettle_skip',
        'series': 'Kitchen tech, decoded',
        'format': 'under_budget',
        'hook_pattern': 'skip_version',
        'title': 'Electric kettle gift: skip the $90 one unless they drink tea',
        'hook_text': 'Skip the $90 kettle',
        'hook_emph': '$90',
        'script': 'Skip the ninety-dollar electric kettle unless they drink tea or make pour-over. In the US, '
                  "most kettles top out around fifteen hundred watts, because that's about what a normal outlet "
                  'can supply, so a twenty-five-dollar kettle boils water about as fast as an expensive one. '
                  'What the extra money buys is temperature control. Green tea tastes best around a hundred '
                  'seventy-five degrees, and pour-over coffee around two hundred, just under boiling. A '
                  'gooseneck spout helps with the slow, even pour. For pasta water and instant oatmeal, the '
                  'basic one is all they need. So ask what they actually make in the morning, and',
        'footage_queries': [   'kettle boiling water',
                               'pouring hot water into cup',
                               'green tea cup',
                               'pour over coffee',
                               'kitchen counter morning',
                               'wrapped gift box'],
        'captions': [{'text': 'Pasta water? Basic is fine', 'at': 'pasta'}],
        'graphics': [   {   'type': 'versus',
                            'at': 'watts',
                            'left': ['$25 kettle', 'about 1500W'],
                            'right': ['$90 kettle', 'about 1500W'],
                            'dur': 3.8},
                        {   'type': 'checklist',
                            'at': 'temperature',
                            'title': 'Worth paying for',
                            'items': ['Green tea: ~175°F', 'Pour-over: ~200°F', 'Gooseneck spout'],
                            'reveal_at': ['green', 'coffee', 'gooseneck']}],
        'hashtags': ['kitchengadgets', 'tea', 'giftideas'],
        'tags': ['electric kettle gift', 'best electric kettle', 'gooseneck kettle'],
        'question': 'Tea, pour-over, or just instant noodles?',
        'affiliate': {   'product_name': 'variable temperature electric kettle',
                         'search_term': 'variable temperature gooseneck electric kettle'}},
    {   'slug': 'kitchen_scale_baking',
        'series': 'Kitchen tech, decoded',
        'format': 'under_budget',
        'hook_pattern': 'price_vs',
        'title': '$15 kitchen scale vs measuring cups: why the same cookies come out different',
        'hook_text': '$15 scale vs measuring cups',
        'hook_emph': '$15',
        'script': 'A fifteen-dollar kitchen scale fixes more baking problems than a new mixer. One cup of flour '
                  'should weigh about a hundred twenty grams, but scoop it straight from the bag and you can '
                  "pack in a quarter more. That's why the same recipe comes out dry one week and fine the next. "
                  'A scale removes the guesswork, and the tare button zeroes out the bowl, so everything goes '
                  'into one bowl with fewer dishes. Look for one that reads in one-gram steps and holds at least '
                  "five kilograms. It's also a good stocking stuffer for anyone who bakes, because",
        'footage_queries': [   'kitchen scale weighing flour',
                               'measuring cup flour',
                               'baking cookies',
                               'mixing bowl baking',
                               'cookies on baking tray',
                               'christmas stocking'],
        'captions': [{'text': 'Tare = zero out the bowl', 'at': 'tare'}],
        'graphics': [   {   'type': 'versus',
                            'at': 'scoop',
                            'left': ['Spooned cup', 'about 120 g'],
                            'right': ['Scooped cup', 'up to ~150 g'],
                            'dur': 4.2},
                        {   'type': 'checklist',
                            'at': 'look',
                            'title': 'Check the scale',
                            'items': ['1 g steps', '5 kg capacity'],
                            'reveal_at': ['onegram', 'kilograms']}],
        'hashtags': ['baking', 'kitchengadgets', 'giftideas'],
        'tags': ['kitchen scale', 'baking gifts', 'stocking stuffers for bakers'],
        'question': 'Do you measure flour by the cup or by weight?',
        'affiliate': {'product_name': 'digital kitchen scale', 'search_term': 'digital kitchen scale grams'}},
    {   'slug': 'tech_gifts_under_50',
        'series': 'Before you buy',
        'format': 'under_budget',
        'hook_pattern': 'one_spec',
        'two_part': {'id': 'giftbudget', 'part': 1},
        'title': "Tech gifts under $50: three that don't end up in a drawer",
        'hook_text': '3 tech gifts under $50',
        'hook_emph': '$50',
        'script': 'Tech gifts under fifty dollars that actually get used each come with one check. A ten '
                  'thousand milliamp hour power bank: make sure it says USB-C P D and at least twenty watts, or '
                  'it charges slowly. A four K streaming stick: check that their TV has a free HDMI port, and '
                  "that they don't already love their smart TV's apps. A tenkeyless mechanical keyboard, like "
                  "the Redragon K552: ask whether they ever use a number pad, because this one doesn't have one. "
                  'A novelty gadget gets used once. These get used every day. So skip the gimmick aisle, because',
        'footage_queries': [   'power bank charging phone',
                               'streaming device tv remote',
                               'mechanical keyboard typing closeup',
                               'wrapped christmas gifts',
                               'person unwrapping gift',
                               'usb c cable plugged in'],
        'captions': [],
        'graphics': [   {   'type': 'checklist',
                            'at': 'power',
                            'title': 'Under $50',
                            'items': ['Power bank: USB-C PD', '4K stick: free HDMI', 'Keyboard: no numpad'],
                            'reveal_at': ['power', 'streaming', 'tenkeyless'],
                            'hold': 1.4},
                        {   'type': 'versus',
                            'at': 'novelty',
                            'left': ['Novelty gadget', 'used once'],
                            'right': ['These three', 'used daily'],
                            'winner': 'right',
                            'reveal_at': ['novelty', 'these']}],
        'hashtags': ['giftideas', 'techgifts', 'techtips'],
        'tags': ['tech gifts under 50', 'gift ideas under 50', 'cheap tech gifts'],
        'question': "What's your gift budget per person this year?",
        'affiliate': {   'product_name': 'USB-C power bank with PD fast charging',
                         'search_term': 'portable charger power bank'}},
    {   'slug': 'tech_gifts_under_100',
        'series': 'Before you buy',
        'format': 'under_budget',
        'hook_pattern': 'one_spec',
        'two_part': {'id': 'giftbudget', 'part': 2},
        'title': 'Tech gifts under $100: three worth the step up',
        'hook_text': '3 tech gifts under $100',
        'hook_emph': '$100',
        'script': 'Tech gifts under a hundred dollars are where you get real upgrades, but each one has a catch '
                  'to check. Noise-cancelling earbuds: look for hybrid A N C and several ear-tip sizes, since '
                  'the seal does most of the work. An instant photo printer like the Kodak Step: Zink paper '
                  'needs no ink, but paper is the ongoing cost, so add a refill pack. A Qi2 magnetic charging '
                  'stand: it fits recent iPhones and the Pixel 10, but most other Android phones need a magnetic '
                  "case. If you don't know their phone, earbuds are the safest bet. So set the budget first, "
                  'because',
        'footage_queries': [   'wireless earbuds case',
                               'person wearing earbuds commute',
                               'instant photo printing',
                               'printed photos on table',
                               'wireless charger phone',
                               'wrapped christmas gifts'],
        'captions': [{'text': "Don't know their phone? Earbuds", 'at': 'safest'}],
        'graphics': [   {   'type': 'checklist',
                            'at': 'hybrid',
                            'title': 'Under $100',
                            'items': ['Earbuds: hybrid ANC', 'Printer: buy refills', 'Qi2 stand: check phone'],
                            'reveal_at': ['hybrid', 'zink', 'magnetic'],
                            'hold': 1.4}],
        'hashtags': ['giftideas', 'techgifts', 'techtips'],
        'tags': ['tech gifts under 100', 'best gifts under 100', 'gift ideas 2026'],
        'question': 'Earbuds, printer or charger: which would they use most?',
        'affiliate': {   'product_name': 'noise cancelling wireless earbuds',
                         'search_term': 'noise cancelling earbuds'}},
    {   'slug': 'coffee_maker_brew_temp',
        'series': 'Kitchen tech, decoded',
        'format': 'comparison',
        'hook_pattern': 'price_vs',
        'title': '$25 vs $150 coffee maker: the difference is water temperature',
        'hook_text': '$25 vs $150 coffee maker',
        'hook_emph': '$25',
        'script': 'A twenty-five-dollar coffee maker and a hundred-fifty-dollar one mostly differ in water '
                  'temperature, not features. Coffee extracts best between about a hundred ninety-five and two '
                  'hundred five degrees. Many cheap drip machines never get the water that hot, so the coffee '
                  'tastes flat and sour, even with good beans. The Specialty Coffee Association certifies home '
                  'brewers that hit that range and finish a full pot in the right time, so look for its '
                  'certified mark on the box or the listing. Timers, apps and fancy carafes are extras. So check '
                  'for that mark before you pay for an app, because',
        'footage_queries': [   'coffee maker brewing',
                               'pouring coffee into mug',
                               'coffee beans closeup',
                               'drip coffee pot',
                               'kitchen counter morning',
                               'coffee cup steam'],
        'captions': [{'text': 'Look for the SCA certified mark', 'at': 'mark'}],
        'graphics': [   {   'type': 'versus',
                            'at': 'cheap',
                            'left': ['Cheap drip', 'often too cool'],
                            'right': ['SCA certified', '195-205°F'],
                            'winner': 'right',
                            'reveal_at': ['cheap', 'certifies'],
                            'hold': 1.2},
                        {   'type': 'checklist',
                            'at': 'timers',
                            'title': 'Extras, not taste',
                            'style': 'avoid',
                            'items': ['Timers', 'Apps'],
                            'reveal_at': ['timers', 'apps']}],
        'hashtags': ['coffee', 'kitchengadgets', 'techtips'],
        'tags': ['best drip coffee maker', 'sca certified coffee maker', 'cheap vs expensive coffee maker'],
        'question': 'Drip, pod, or French press at your place?'},
    {   'slug': 'projector_gift_of_week',
        'series': 'Gift of the week',
        'format': 'gift_pick',
        'hook_pattern': 'one_spec',
        'title': 'Mini projector gift: check for a real Netflix app before you buy',
        'hook_text': 'Projector gift? Check Netflix',
        'hook_emph': 'Netflix',
        'script': "A mini projector is a great gift for kids' movie nights, a dorm room or the backyard, but "
                  'check one thing first: does it run Netflix natively? Many cheap projectors use a generic '
                  "Android system, and Netflix often won't install, or only plays through screen mirroring. Look "
                  "for Google TV or Fire TV built in, or plan to add a streaming stick and make sure there's an "
                  'HDMI port. Then check the two specs that matter: native full HD, not just four K supported, '
                  'and two to three hundred ANSI lumens for a dark room. Get those right, and',
        'footage_queries': [   'movie night projector screen',
                               'home projector on table',
                               'family watching movie at home',
                               'projector light beam',
                               'streaming device tv remote',
                               'dorm room'],
        'captions': [],
        'graphics': [   {   'type': 'versus',
                            'at': 'generic',
                            'left': ['Generic', 'Netflix may fail'],
                            'right': ['Google TV', 'or Fire TV built in'],
                            'winner': 'right',
                            'reveal_at': ['generic', 'google'],
                            'hold': 1.6},
                        {   'type': 'checklist',
                            'at': 'specs',
                            'title': 'Then check',
                            'items': ['Native full HD', '200-300 ANSI lumens'],
                            'reveal_at': ['native', 'ansi']}],
        'hashtags': ['projector', 'giftideas', 'movienight'],
        'tags': ['projector gift', 'best mini projector', 'projector with netflix'],
        'question': 'Would you watch movies on a wall instead of a TV?',
        'affiliate': {   'product_name': '1080p mini projector with Google TV',
                         'search_term': '1080p mini projector google tv netflix'}},
    {   'slug': 'monitor_1080_vs_1440',
        'series': 'Before you buy',
        'format': 'comparison',
        'hook_pattern': 'price_vs',
        'title': '$120 vs $250 monitor: why 1080p looks soft at 27 inches',
        'hook_text': '$120 vs $250 monitor',
        'hook_emph': '$120',
        'script': 'A hundred-twenty-dollar full HD monitor looks sharp at twenty-four inches and soft at '
                  "twenty-seven. It's the same number of pixels stretched across a bigger screen: about "
                  'ninety-two pixels per inch at twenty-four inches, but only eighty-two at twenty-seven. Text '
                  'looks fuzzy, and up close you can see the grid. A Quad HD panel at twenty-seven inches packs '
                  "about a hundred nine pixels per inch, which is why it's the sweet spot for work and gaming, "
                  'often for around a hundred dollars more. So get full HD at twenty-four inches, or Quad HD at '
                  'twenty-seven, and match the resolution to the size, because',
        'footage_queries': [   'computer monitor on desk',
                               'home office desk setup',
                               'typing on keyboard monitor',
                               'gaming setup monitor',
                               'spreadsheet on computer screen',
                               'person working at desk'],
        'captions': [{'text': '24in full HD, 27in Quad HD', 'at': 'get'}],
        'graphics': [   {   'type': 'specs',
                            'at': 'stretched',
                            'title': 'Pixels per inch',
                            'rows': [['24 in full HD', '92'], ['27 in full HD', '82'], ['27 in Quad HD', '109']],
                            'highlight': 3,
                            'reveal_at': ['ninetytwo', 'eightytwo', 'quad'],
                            'source': 'source: screen size + resolution math'}],
        'hashtags': ['desksetup', 'monitor', 'techtips'],
        'tags': ['1080p vs 1440p', 'best 27 inch monitor', 'budget monitor'],
        'question': 'What size monitor is on your desk?',
        'affiliate': {'product_name': '27 inch 1440p monitor', 'search_term': '27 inch 1440p monitor'}},
    {
        "slug": "delivery_text_scam",
        "series": "Security in 30 seconds",
        "format": "red_flag",
        "hook_pattern": "one_spec",
        "title": "That 'package couldn't be delivered' text is a holiday scam",
        "hook_text": "USPS doesn't text you links",
        "hook_emph": "links",
        "script": (
            "Real delivery companies don't text you a link to pay a redelivery fee. That text is one of the most "
            "common holiday scams. It claims USPS, FedEx or UPS missed your package and asks you to confirm your "
            "address or pay a small fee. The link leads to a copycat site that steals your card number. USPS says "
            "it doesn't text links unless you asked for tracking. To check a real package, open the carrier's app "
            "with the store's tracking number. Then forward the text to seven, seven, two, six, because"
        ),
        "footage_queries": ["package on doorstep", "phone text message notification", "delivery truck",
                            "entering credit card online", "typing on smartphone", "delivery man with box"],
        "captions": [{"text": "Forward scam texts to 7726", "at": "forward"}],
        "graphics": [
            {"type": "checklist", "at": "confirm", "title": "Red flags", "style": "avoid",
             "items": ["Confirm your address", "Pay a small fee"], "reveal_at": ["confirm", "fee"], "hold": 1.6},
            {"type": "steps", "at": "check", "title": "Check it safely",
             "items": ["Open the carrier's app", "Use the store's tracking #"], "reveal_at": ["app", "tracking"]},
        ],
        "hashtags": ["scam", "cybersecurity", "techtips"],
        "tags": ["usps text scam", "package delivery scam", "smishing"],
        "question": "Have you gotten one of these texts yet?",
    },
    {
        "slug": "power_bank_plane_rule",
        "series": "Charging, decoded",
        "format": "before_you_buy",
        "hook_pattern": "one_spec",
        "title": "Flying for the holidays? The power bank limit is in watt hours",
        "hook_text": "Power bank? Carry-on only",
        "hook_emph": "Carry-on",
        "script": (
            "A power bank in your checked bag can get pulled at the airport, because spare lithium batteries have "
            "to fly in the cabin. The limit that matters is a hundred watt hours, not milliamp hours. To convert, "
            "multiply the milliamp hours by three point seven and divide by a thousand. A twenty thousand milliamp "
            "hour bank is about seventy-four watt hours, so it's fine. Around twenty-seven thousand, you hit the "
            "limit, and bigger ones need airline approval. Some airlines now ban using power banks during the "
            "flight, so check before you board, and pack it in your carry-on, because"
        ),
        "footage_queries": ["charging phone with power bank", "airport security line", "suitcase packing",
                            "airplane cabin passengers", "airplane overhead bin", "phone charging on airplane"],
        "captions": [{"text": "mAh x 3.7 / 1,000 = Wh", "at": "multiply"}],
        "graphics": [
            {"type": "specs", "at": "about", "title": "Carry-on limit: 100 Wh",
             "rows": [["20,000 mAh", "~74 Wh"], ["27,000 mAh", "~100 Wh"]],
             "highlight": 1, "source": "source: FAA lithium battery rules", "dur": 4.6},
            {"type": "checklist", "at": "airlines", "title": "Before you fly",
             "items": ["Carry-on, never checked", "Check the airline's rules"], "reveal_at": ["airlines", "pack"]},
        ],
        "hashtags": ["travel", "powerbank", "techtips"],
        "tags": ["power bank on plane", "tsa power bank rules", "100wh power bank"],
        "question": "How big is the power bank in your bag?",
    },

    # ---- Nov 9 2026 weekly batch (14 new, interleaved): kitchen tech leads (air fryer 1,220 views day 1,
    # grinder/thermometer/SSD all 120-330/day). Black Friday deal-literacy ~Nov 15-21, Secret Santa pair and
    # "gifts for dad" timed for recipient searches Nov 22-24. Weak settings/security tips moved to the back.
    {   'slug': 'hand_vs_stand_mixer_gift',
        'series': 'Kitchen tech, decoded',
        'format': 'comparison',
        'hook_pattern': 'price_vs',
        'title': "$40 hand mixer vs $400 stand mixer: which gift they'll actually use",
        'hook_text': '$40 vs $400 mixer',
        'hook_emph': '$400',
        'script': 'A forty-dollar hand mixer handles most of what people bake. Cookie dough, whipped cream, cake '
                  'batter and mashed potatoes are all quick jobs for a five-speed hand mixer, and it fits in a '
                  'drawer. A stand mixer, often four hundred dollars or more for a KitchenAid Artisan, earns its '
                  "price with heavy bread dough, double batches and long mixing you don't want to hold. It also "
                  'weighs over twenty pounds, so it needs a permanent spot on the counter. So ask one question: '
                  'do they bake bread or big batches most weeks? If not, give the hand mixer, because',
        'footage_queries': [   'mixing batter in bowl',
                               'cookie dough baking',
                               'whipped cream',
                               'cake batter',
                               'stand mixer kitchen',
                               'kneading bread dough',
                               'wrapped christmas gifts'],
        'captions': [{'text': 'Bread every week? Stand mixer', 'at': 'question'}],
        'graphics': [   {   'type': 'checklist',
                            'at': 'cookie',
                            'title': 'A hand mixer handles',
                            'items': ['Cookie dough', 'Whipped cream', 'Cake batter'],
                            'reveal_at': ['cookie', 'whipped', 'cake']},
                        {   'type': 'versus',
                            'at': 'stand',
                            'left': ['Hand mixer', '~$40, fits a drawer'],
                            'right': ['Stand mixer', '~$400, 20+ lb'],
                            'dur': 4.0}],
        'hashtags': ['kitchengadgets', 'giftideas', 'baking'],
        'tags': ['hand mixer vs stand mixer', 'kitchenaid stand mixer gift', 'kitchen gifts', 'gifts for bakers'],
        'question': 'Hand mixer or stand mixer in your kitchen?',
        'affiliate': {'product_name': '5-speed hand mixer', 'search_term': 'kitchenaid 5 speed hand mixer'}},
    {
        "slug": "tv_motion_rate_trap",
        "series": "Before you buy",
        "format": "before_you_buy",
        "hook_pattern": "one_spec",
        "title": "Buying a TV for Black Friday? 'Motion Rate 240' isn't 240Hz",
        "hook_text": "Motion Rate 240 isn't 240Hz",
        "hook_emph": "240",
        "script": (
            "That Motion Rate two hundred forty on a TV box usually isn't the screen's real refresh rate. Brands use names "
            "like Motion Rate, TruMotion or Motionflow for a processed figure that's often double the panel's "
            "native rate. A Motion Rate two hundred forty TV is very often a native one hundred twenty hertz panel, and Motion Rate "
            "one hundred twenty is often native sixty. That's fine for movies and regular TV. Native one hundred twenty matters for sports and for gaming on a "
            "PlayStation five or Xbox Series X. So search the model number plus native refresh rate before you "
            "buy, because"
        ),
        "footage_queries": ["television living room", "tv store display", "watching football on tv",
                            "playing video games console", "tv remote closeup", "electronics store shopping"],
        "captions": [{"text": "Search: model + native refresh rate", "at": "search"}],
        "graphics": [
            {"type": "versus", "at": "processed", "left": ["On the box", "Motion Rate 240"],
             "right": ["Real panel", "often 120Hz"], "winner": "right", "dur": 4.6},
            {"type": "checklist", "at": "matters", "title": "Native 120Hz helps",
             "items": ["Sports", "PS5 / Xbox Series X"], "reveal_at": ["sports", "gaming"]},
        ],
        "hashtags": ["tv", "blackfriday", "techtips"],
        "tags": ["black friday tv", "120hz vs 60hz tv", "motion rate 240"],
        "question": "What refresh rate is your TV, really?",
    },
    {   'slug': 'dual_basket_air_fryer',
        'series': 'Kitchen tech, decoded',
        'format': 'before_you_buy',
        'hook_pattern': 'one_spec',
        'title': 'Dual basket air fryer: 8 quarts is really two 4-quart baskets',
        'hook_text': '8 quarts? Check each basket',
        'hook_emph': 'each basket',
        'script': "A dual basket air fryer marked eight quarts is really two four-quart baskets. That's great "
                  'when dinner has two parts. You can run chicken in one and fries in the other, and on models '
                  'like the Ninja DualZone, a sync button makes both finish at the same time. But a big roast or '
                  'a family batch of wings has to fit in one four-quart basket, and food only crisps in a single '
                  'layer. So for two-part meals, get dual baskets. For one big dish, a single basket of six '
                  'quarts or more holds more. Check the size of each basket, because',
        'footage_queries': [   'air fryer cooking',
                               'chicken wings',
                               'french fries',
                               'family dinner table',
                               'roast chicken',
                               'kitchen countertop appliances'],
        'captions': [{'text': 'Sync = both finish together', 'at': 'sync'}],
        'graphics': [   {   'type': 'versus',
                            'at': 'dinner',
                            'left': ['The label', '8 quarts'],
                            'right': ['Each basket', '4 quarts'],
                            'winner': 'right'},
                        {   'type': 'checklist',
                            'at': 'meals',
                            'title': 'Which one?',
                            'items': ['Two-part meals: dual', 'One big dish: single 6 qt+'],
                            'reveal_at': ['meals', 'dish']}],
        'hashtags': ['airfryer', 'kitchengadgets', 'techtips'],
        'tags': ['dual basket air fryer', 'ninja dual zone air fryer', 'best air fryer for family'],
        'question': 'What would you cook in two baskets at once?',
        'affiliate': {'product_name': '8-quart dual-basket air fryer', 'search_term': 'ninja dualzone air fryer'}},
    {   'slug': 'black_friday_price_history',
        'series': 'Before you buy',
        'format': 'before_you_buy',
        'hook_pattern': 'dont_until',
        'title': "Black Friday 'was' prices: check the price history first",
        'hook_text': "Don't trust the 'was' price",
        'hook_emph': "'was'",
        'script': "Don't trust a Black Friday was price until you check the price history. Retailers can show a "
                  'high reference price the product rarely sold at, so forty percent off might just be the '
                  'normal price. Free tools fix that in seconds. For Amazon, paste the product link into Camel '
                  "Camel Camel, or install the Keepa extension, and you'll see a chart of past prices. Google "
                  'Shopping shows price history on many products too. A real deal sits at or near the lowest '
                  "point on that chart. If last month's price was the same, it isn't a deal. So before you check "
                  'out,',
        'footage_queries': [   'online shopping laptop',
                               'black friday shopping',
                               'price tag closeup',
                               'shopping cart online',
                               'person shopping on phone',
                               'shopping bags store'],
        'captions': [],
        'graphics': [   {   'type': 'steps',
                            'at': 'amazon',
                            'title': 'Check the history',
                            'items': ['CamelCamelCamel', 'Keepa extension', 'Google Shopping'],
                            'reveal_at': ['camel', 'keepa', 'google'],
                            'hold': 1.0},
                        {   'type': 'versus',
                            'at': 'real',
                            'left': ['Real deal', 'near the low'],
                            'right': ['Not a deal', 'same as last month'],
                            'winner': 'left',
                            'reveal_at': ['real', 'month']}],
        'hashtags': ['blackfriday', 'shoppingtips', 'techtips'],
        'tags': ['black friday deals', 'price history checker', 'camelcamelcamel'],
        'question': 'What are you waiting for Black Friday to buy?'},
    {   'slug': 'turkey_probe_thermometer',
        'series': 'Kitchen tech, decoded',
        'format': 'comparison',
        'hook_pattern': 'one_spec',
        'title': 'Meat thermometer for turkey: why a leave-in probe beats instant-read',
        'hook_text': 'Turkey? Use a leave-in probe',
        'hook_emph': 'leave-in',
        'script': 'A meat thermometer for turkey works best when it stays in the bird. An instant-read '
                  'thermometer checks in a few seconds, but every check means opening the oven and letting the '
                  "heat out. A leave-in probe stays in the thickest part the whole time and alerts you when it's "
                  'close. The USDA says turkey is safe at a hundred sixty-five degrees, checked in the breast, '
                  'the innermost thigh and the wing. Then let it rest about twenty minutes before carving. '
                  'Wireless probes are handy, but a wired probe with a display costs less and works the same. So '
                  'this Thanksgiving, remember that',
        'footage_queries': ['roasted chicken in oven', 'oven door opening', 'roast meat on cutting board', 'carving roast meat', 'kitchen oven cooking', 'family dinner table'],
        'captions': [{'text': 'Rest ~20 min before carving', 'at': 'rest'}],
        'graphics': [   {   'type': 'versus',
                            'at': 'seconds',
                            'left': ['Instant', 'oven opens'],
                            'right': ['Leave-in probe', 'stays in'],
                            'winner': 'right',
                            'reveal_at': ['seconds', 'probe']},
                        {   'type': 'specs',
                            'at': 'safe',
                            'title': 'Turkey is done at',
                            'rows': [['Breast', '165°F'], ['Thigh', '165°F'], ['Wing', '165°F']],
                            'reveal_at': ['breast', 'thigh', 'wing'],
                            'source': 'source: USDA FSIS'}],
        'hashtags': ['thanksgiving', 'kitchengadgets', 'cookingtips'],
        'tags': ['meat thermometer for turkey', 'turkey temperature', 'leave in meat thermometer'],
        'question': "Who's cooking the turkey at your place this year?",
        'affiliate': {   'product_name': 'leave-in probe meat thermometer',
                         'search_term': 'leave in probe meat thermometer'}},
    {   'slug': 'travel_65w_charger',
        'series': 'Charging, decoded',
        'format': 'under_budget',
        'hook_pattern': 'one_spec',
        'title': 'One 65W USB-C charger can replace three bricks: check your laptop first',
        'hook_text': 'One 65W charger for all',
        'hook_emph': '65W',
        'script': 'One sixty-five-watt USB-C charger can replace your laptop brick, phone charger and tablet '
                  'charger for holiday travel. Newer GaN chargers are about the size of a phone charger from a '
                  'few years ago. Two checks first. Your laptop has to charge over USB-C. Round barrel plugs '
                  "won't work. And look at the wattage printed on its original charger: most thin laptops need "
                  'forty-five to sixty-five watts. When both ports are in use, the power splits, often '
                  "forty-five for the laptop and twenty for the phone. That's plenty overnight. So before you "
                  'pack a tangle of bricks, remember that',
        'footage_queries': [   'laptop charging',
                               'packing suitcase travel',
                               'phone charging',
                               'usb c port laptop',
                               'airport travel',
                               'hotel room desk'],
        'captions': [{'text': 'Both ports: often 45W + 20W', 'at': 'splits'}],
        'graphics': [   {   'type': 'checklist',
                            'at': 'checks',
                            'title': 'Check first',
                            'items': ['Laptop charges by USB-C', 'Its brick: 45-65W'],
                            'reveal_at': ['laptop', 'wattage'],
                            'hold': 1.4}],
        'hashtags': ['travel', 'charger', 'techtips'],
        'tags': ['65w usb c charger', 'travel charger', 'laptop usb c charger'],
        'question': 'How many chargers are in your bag right now?',
        'affiliate': {   'product_name': '65W 2-port USB-C GaN charger',
                         'search_term': '65W USB C GaN charger 2 port'}},
    {   'slug': 'coffee_maker_smart_plug',
        'series': 'Kitchen tech, decoded',
        'format': 'before_you_buy',
        'hook_pattern': 'one_spec',
        'title': 'A $10 smart plug can start your coffee, but only with this kind of switch',
        'hook_text': '$10 smart plug coffee check',
        'hook_emph': '$10',
        'script': 'A ten-dollar smart plug can start your coffee before your alarm goes off, but only if the '
                  'coffee maker has the right kind of switch. Look for a physical switch that stays on when you '
                  'unplug the machine and plug it back in. Many newer machines use a soft-touch button that '
                  "resets to off when power returns, and a smart plug can't press that. Most smart plugs are "
                  'rated fifteen amps, which covers a typical coffee maker, and many only connect to two point '
                  'four gigahertz Wi-Fi. Test it once: unplug, plug back in, and see if it brews. If it does, '
                  'then',
        'footage_queries': [   'coffee maker brewing',
                               'smart plug',
                               'alarm clock morning',
                               'pouring coffee into mug',
                               'phone app smart home',
                               'kitchen counter morning'],
        'captions': [{'text': 'Most need 2.4 GHz Wi-Fi', 'at': 'gigahertz'}],
        'graphics': [   {   'type': 'versus',
                            'at': 'physical',
                            'left': ['Toggle switch', 'stays on: works'],
                            'right': ['Push button', 'resets to off'],
                            'winner': 'left',
                            'reveal_at': ['physical', 'soft'],
                            'hold': 1.4},
                        {   'type': 'steps',
                            'at': 'test',
                            'items': ['Unplug, plug back in', 'Does it brew?'],
                            'reveal_at': ['unplug', 'brews']}],
        'hashtags': ['smarthome', 'coffee', 'techtips'],
        'tags': ['smart plug coffee maker', 'smart home ideas', 'automatic coffee maker'],
        'question': 'Would you trust a timer with your morning coffee?'},
    {   'slug': 'black_friday_what_to_buy',
        'series': 'Before you buy',
        'format': 'comparison',
        'hook_pattern': 'price_vs',
        'title': "Black Friday: what's usually worth buying, and what to wait on",
        'hook_text': 'Black Friday: buy or wait?',
        'hook_emph': 'buy',
        'script': 'Black Friday deals are usually real on four kinds of tech: TVs, earbuds, e-readers, and '
                  "Amazon's own devices like Echo speakers and Fire TV sticks. Those often hit their lowest "
                  "prices of the year that week. Chargers, cables and storage drives drop too, and they're easy "
                  'wins. Brand-new flagship phones are the exception. Most of their deals depend on a carrier '
                  'plan, a new line or a trade-in, so read the fine print before you call it a discount. The '
                  'same goes for anything released in the last month or two. So make two lists before the sale '
                  'starts, because',
        'footage_queries': [   'black friday shopping',
                               'television living room',
                               'wireless earbuds case',
                               'reading e-reader',
                               'smart speaker closeup',
                               'smartphone store display'],
        'captions': [{'text': 'Phone deals: read the fine print', 'at': 'fine'}],
        'graphics': [   {   'type': 'checklist',
                            'at': 'tvs',
                            'title': 'Usually worth it',
                            'items': ['TVs', 'Earbuds', 'E-readers', 'Amazon devices'],
                            'reveal_at': ['tvs', 'earbuds', 'ereaders', 'amazons'],
                            'hold': 1.2},
                        {   'type': 'checklist',
                            'at': 'flagship',
                            'title': 'Usually wait',
                            'style': 'avoid',
                            'items': ['New flagship phones', 'Just-released gadgets'],
                            'reveal_at': ['flagship', 'released']}],
        'hashtags': ['blackfriday', 'techdeals', 'techtips'],
        'tags': ['black friday tech deals', 'what to buy on black friday', 'black friday 2026'],
        'question': 'TV, earbuds or something else on your list?'},
    {   'slug': 'bluetooth_speaker_gift_of_week',
        'series': 'Gift of the week',
        'format': 'gift_pick',
        'hook_pattern': 'one_spec',
        'title': 'Bluetooth speaker gift: check for IP67 before you buy',
        'hook_text': 'Speaker gift? Check IP67',
        'hook_emph': 'IP67',
        'script': "A Bluetooth speaker gift is only as good as the places it survives. That's what the I P "
                  'rating tells you. I P sixty-seven means dust-tight and able to sit in about a meter of water '
                  'for thirty minutes, so the beach, the shower and a spilled drink are covered. I P X four only '
                  'covers splashes. Small clip-on speakers like the JBL Clip 5 are rated I P sixty-seven and '
                  'hang off a bag, which suits teens, hikers and anyone who showers with music. The one thing to '
                  'check before buying is battery life on the spec sheet. Look for ten hours or more, because',
        'footage_queries': [   'bluetooth speaker',
                               'friends at the beach',
                               'shower water running',
                               'hiking backpack trail',
                               'teenager listening to music',
                               'wrapped christmas gifts'],
        'captions': [{'text': 'Who: teens, hikers, shower singers', 'at': 'teens'}],
        'graphics': [   {   'type': 'specs',
                            'at': 'rating',
                            'title': 'Water ratings',
                            'rows': [['IP67', '1 m for 30 min'], ['IPX4', 'splashes only']],
                            'reveal_at': ['meter', 'splashes'],
                            'source': 'source: IEC 60529'},
                        {   'type': 'checklist',
                            'at': 'battery',
                            'title': 'Before you buy',
                            'items': ['IP67 rating', '10+ hours battery'],
                            'reveal_at': ['battery', 'hours']}],
        'hashtags': ['giftideas', 'bluetoothspeaker', 'techgifts'],
        'tags': ['bluetooth speaker gift', 'waterproof bluetooth speaker', 'gifts for teens'],
        'question': 'Where would they use a speaker most?',
        'affiliate': {'product_name': 'IP67 clip-on Bluetooth speaker', 'search_term': 'jbl clip 5'}},
    {   'slug': 'black_friday_laptop_ram',
        'series': 'Before you buy',
        'format': 'before_you_buy',
        'hook_pattern': 'dont_until',
        'title': "Don't buy a $400 Black Friday laptop until you check the RAM",
        'hook_text': '$400 laptop? Check the RAM',
        'hook_emph': 'RAM',
        'script': 'On a cheap Black Friday laptop, the RAM decides whether it still feels fast next year. Eight '
                  'gigabytes runs Windows 11, but with a browser full of tabs and a video call, it slows down '
                  'quickly. Sixteen is the comfortable floor now. Microsoft requires it for Copilot Plus PCs, '
                  'and every new MacBook Air starts there. Check one more thing: many budget laptops solder the '
                  "RAM to the board, so you can't add more later. Storage matters too, so look for an SSD of at "
                  'least two hundred fifty-six gigabytes. A doorbuster with only eight is rarely the deal '
                  'it looks like. So before you check out, remember that',
        'footage_queries': ['laptop keyboard typing closeup', 'laptop screen closeup', 'video call on laptop', 'computer memory ram', 'person using laptop at home', 'online shopping laptop'],
        'captions': [],
        'graphics': [   {   'type': 'specs',
                            'at': 'tabs',
                            'title': 'Laptop RAM',
                            'rows': [['8 GB', 'slows with tabs'], ['16 GB', 'comfortable floor']],
                            'reveal_at': ['tabs', 'sixteen'],
                            'source': 'Copilot+ PC minimum: 16 GB (Microsoft)'},
                        {   'type': 'checklist',
                            'at': 'solder',
                            'title': 'Before checkout',
                            'items': ['16 GB RAM', 'Soldered? No upgrades', '256 GB+ SSD'],
                            'reveal_at': ['solder', 'later', 'storage']}],
        'hashtags': ['blackfriday', 'laptop', 'techtips'],
        'tags': ['black friday laptop', '8gb vs 16gb ram', 'best cheap laptop'],
        'question': 'How much RAM does your laptop have?'},
    {   'slug': 'espresso_machine_grinder',
        'series': 'Kitchen tech, decoded',
        'format': 'before_you_buy',
        'hook_pattern': 'one_spec',
        'title': 'Espresso machine gift? The grinder matters more than the machine',
        'hook_text': 'Espresso gift? Grinder first',
        'hook_emph': 'grinder',
        'script': 'Home espresso depends more on the grinder than the machine. Espresso needs coffee ground very '
                  'fine and very evenly, and most pre-ground bags are too coarse. Budget machines get around '
                  'that with a pressurized basket, which fakes the crema but caps how good the shot can get. To '
                  'use a regular basket, you need a burr grinder made for espresso, and those often start around '
                  "a hundred fifty dollars. So before you gift a machine, check what they'd grind with. If the "
                  'answer is nothing, a pod machine or a moka pot is the easier gift, because',
        'footage_queries': [   'espresso machine',
                               'espresso shot pouring',
                               'coffee grinder',
                               'ground coffee closeup',
                               'moka pot stove',
                               'coffee capsule machine'],
        'captions': [{'text': 'Budget espresso grinders: ~$150+', 'at': 'grinder'}],
        'graphics': [   {   'type': 'versus',
                            'at': 'pressurized',
                            'left': ['Easy basket', 'capped shots'],
                            'right': ['Regular basket', 'needs a fine grinder'],
                            'reveal_at': ['pressurized', 'regular']},
                        {   'type': 'checklist',
                            'at': 'nothing',
                            'title': 'No grinder? Give',
                            'items': ['A pod machine', 'A moka pot'],
                            'reveal_at': ['pod', 'moka']}],
        'hashtags': ['coffee', 'espresso', 'giftideas'],
        'tags': ['espresso machine gift', 'best espresso machine for beginners', 'espresso grinder'],
        'question': 'Pods, moka pot or espresso at your place?'},
    {   'slug': 'last_year_earbuds_black_friday',
        'series': 'Before you buy',
        'format': 'comparison',
        'hook_pattern': 'price_vs',
        'title': "Black Friday earbuds: last year's model is often the better buy",
        'hook_text': "Last year's earbuds: the deal",
        'hook_emph': "Last year's",
        'script': "On Black Friday, last year's flagship earbuds are often a better buy than this year's. When a "
                  'new model launches, the old one usually gets the deepest discounts, while the new one sees '
                  'small ones. The noise cancelling is often close. What the newer pair usually adds is a little '
                  'more playtime, a newer chip or a health sensor. So compare the two on three things: noise '
                  'cancelling reviews, battery hours and whether the case charges over USB-C. If the older pair '
                  'matches on all three, the savings are real. Also check that it still gets firmware updates, '
                  'because',
        'footage_queries': [   'wireless earbuds case',
                               'person wearing earbuds',
                               'online shopping laptop',
                               'earbuds charging case',
                               'commuter wearing earbuds',
                               'black friday shopping'],
        'captions': [],
        'graphics': [   {   'type': 'versus',
                            'at': 'launches',
                            'left': ['New model', 'small discounts'],
                            'right': ["Last year's", 'deepest discounts'],
                            'winner': 'right'},
                        {   'type': 'checklist',
                            'at': 'compare',
                            'title': 'Compare on 3 things',
                            'items': ['ANC reviews', 'Battery hours', 'USB-C case'],
                            'reveal_at': ['reviews', 'battery', 'case']}],
        'hashtags': ['blackfriday', 'earbuds', 'techtips'],
        'tags': ['black friday earbuds', 'best earbuds deal', 'airpods pro black friday'],
        'question': "Would you buy last year's model to save money?"},
    {   'slug': 'robot_vacuum_lidar',
        'series': 'Before you buy',
        'format': 'before_you_buy',
        'hook_pattern': 'one_spec',
        'title': 'Robot vacuum on sale? Check for lidar before you buy',
        'hook_text': 'Robot vacuum? Check for lidar',
        'hook_emph': 'lidar',
        'script': 'The spec that decides how well a robot vacuum cleans is how it navigates. The cheapest models '
                  'bump around at random, so they miss spots and take far longer. Models with lidar, the small '
                  'spinning turret on top, map each room, clean in neat rows and let you block off areas in the '
                  'app. Lidar models now often sell for under two hundred fifty dollars on sale, not far from '
                  'bump-and-go ones. Check two more things: whether it saves maps for more than one floor, and '
                  'whether the dustbin needs emptying after every run. So when the sale prices drop, remember '
                  'that',
        'footage_queries': [   'robot vacuum cleaner',
                               'robot vacuum living room',
                               'clean living room floor',
                               'phone app smart home',
                               'robot vacuum on carpet',
                               'robot vacuum cleaning floor'],
        'captions': [],
        'graphics': [   {   'type': 'versus',
                            'at': 'random',
                            'left': ['Random bump', 'misses spots'],
                            'right': ['Lidar', 'maps rooms, neat rows'],
                            'winner': 'right',
                            'reveal_at': ['random', 'lidar']},
                        {   'type': 'checklist',
                            'at': 'floor',
                            'title': 'Also check',
                            'items': ['Maps for each floor', 'Bin emptying'],
                            'reveal_at': ['floor', 'dustbin']}],
        'hashtags': ['robotvacuum', 'smarthome', 'blackfriday'],
        'tags': ['robot vacuum black friday', 'lidar robot vacuum', 'best budget robot vacuum'],
        'question': 'Would you trust a robot vacuum with your floors?',
        'affiliate': {'product_name': 'lidar robot vacuum', 'search_term': 'lidar robot vacuum'}},
    {   'slug': 'gift_card_drain',
        'series': 'Security in 30 seconds',
        'format': 'red_flag',
        'hook_pattern': 'one_spec',
        'title': 'Check the back of a gift card before you buy it off the rack',
        'hook_text': '$100 gift card, already empty',
        'hook_emph': '$100',
        'script': 'A hundred-dollar gift card can be drained before the person you gave it to even opens it. '
                  'Scammers peel open cards on store racks, copy the number and PIN, and reseal them. Once you '
                  'pay and the card is activated, they spend the balance. So flip it over before you buy. Pass '
                  'on any card with torn packaging, a scratched PIN strip, or a sticker over the numbers. And '
                  'anyone asking you to pay a bill with gift cards is a scammer. Buy from behind the counter or '
                  "the brand's own website, and keep the receipt, because",
        'footage_queries': [   'gift card',
                               'holding gift card',
                               'store shelf shopping',
                               'person paying at checkout',
                               'receipt closeup',
                               'online shopping laptop'],
        'captions': [{'text': 'Bill paid in gift cards = scam', 'at': 'bill'}],
        'graphics': [   {   'type': 'checklist',
                            'at': 'flip',
                            'title': 'Pass on it if',
                            'style': 'avoid',
                            'items': ['Torn packaging', 'Scratched PIN strip', 'Sticker over numbers'],
                            'reveal_at': ['torn', 'scratched', 'sticker'],
                            'hold': 1.2}],
        'hashtags': ['scamalert', 'giftcards', 'cybersecurity'],
        'tags': ['gift card scam', 'gift card draining', 'holiday scams'],
        'question': 'Have you ever had a gift card come up empty?'},
    {   'slug': 'tv_size_black_friday',
        'series': 'Before you buy',
        'format': 'comparison',
        'hook_pattern': 'price_vs',
        'title': '55 vs 65 inch TV: measure your couch distance first',
        'hook_text': '55 vs 65 inch TV: measure',
        'hook_emph': '65',
        'script': 'Whether a sixty-five-inch TV is too big depends on one measurement: how far your couch is '
                  'from the screen. For four K, a common guideline is to sit about one to one and a half times '
                  'the screen size away. So a fifty-five-inch TV fits about four and a half to seven feet, and a '
                  'sixty-five fits roughly five and a half to eight. Sit much farther back and the extra detail '
                  'is hard to see. On Black Friday the price gap between those two sizes is often smaller than '
                  'people expect, so measure before you shop. Grab a tape measure tonight, because',
        'footage_queries': [   'living room tv',
                               'couch living room',
                               'tape measure',
                               'watching tv on couch',
                               'tv store display',
                               'family watching tv'],
        'captions': [{'text': 'Measure couch to screen', 'at': 'measure'}],
        'graphics': [   {   'type': 'specs',
                            'at': 'guideline',
                            'title': '4K viewing distance',
                            'rows': [['55-inch', '4.5-7 ft'], ['65-inch', '5.5-8 ft']],
                            'reveal_at': ['fits', 'roughly'],
                            'source': 'guideline: 1-1.5x the screen size'}],
        'hashtags': ['blackfriday', 'tv', 'techtips'],
        'tags': ['55 vs 65 inch tv', 'what size tv should i get', 'black friday tv'],
        'question': 'How far is your couch from your TV?'},
    {   'slug': 'fake_deal_sites',
        'series': 'Security in 30 seconds',
        'format': 'red_flag',
        'hook_pattern': 'dont_until',
        'title': "Don't buy from a 70% off holiday ad until you check these 3 things",
        'hook_text': '70% off ad? Check the URL',
        'hook_emph': '70% off',
        'script': 'A seventy percent off ad for a brand-name gadget is one of the most common holiday scams. '
                  'Fake shops copy real store pages and run social media ads, then ship nothing or a cheap '
                  'knockoff. Check three things before you pay. The web address: look for a misspelled brand or '
                  "an odd ending. The site's age: a quick domain lookup shows if it was registered weeks ago. "
                  'And how you pay: use a credit card, not debit, because U.S. law limits your liability for '
                  'unauthorized credit card charges at fifty dollars, and disputes are easier. So the next time '
                  'a deal looks too good, remember that',
        'footage_queries': [   'online shopping on phone',
                               'scrolling social media phone',
                               'typing on laptop',
                               'credit card payment online',
                               'package delivery doorstep',
                               'black friday sale sign'],
        'captions': [],
        'graphics': [   {   'type': 'checklist',
                            'at': 'three',
                            'title': 'Before you pay',
                            'items': ['Web address spelling', 'Domain age', 'Credit card, not debit'],
                            'reveal_at': ['address', 'age', 'credit']}],
        'hashtags': ['scamalert', 'blackfriday', 'cybersecurity'],
        'tags': ['black friday scams', 'fake online stores', 'is this website legit'],
        'question': 'Have you ever seen a deal ad that looked too good?'},
    {   'slug': 'secret_santa_under_25',
        'series': 'Before you buy',
        'format': 'under_budget',
        'hook_pattern': 'one_spec',
        'two_part': {'id': 'secretsanta', 'part': 1},
        'title': 'Secret Santa gift ideas under $25: three that work for anyone',
        'hook_text': 'Secret Santa under $25',
        'hook_emph': '$25',
        'script': 'Secret Santa gifts under twenty-five dollars work best when they fit any phone and any home. '
                  'A USB-C wall charger with twenty watts or more charges recent iPhones and most Android phones '
                  'fast, and nearly everyone still has a slow old brick. A rechargeable book light clips on or '
                  'wraps around the neck, so it suits anyone who reads in bed. And a smart plug puts a lamp on a '
                  'schedule from their phone. Just check that it works with the voice assistant they use, if '
                  "any. All three get used the same week they're unwrapped. So when you barely know who you "
                  'drew,',
        'footage_queries': [   'christmas gift exchange',
                               'phone charging',
                               'reading in bed at night',
                               'lamp turning on',
                               'smart home phone app',
                               'wrapped christmas gifts'],
        'captions': [{'text': 'Check their voice assistant', 'at': 'assistant'}],
        'graphics': [   {   'type': 'checklist',
                            'at': 'charger',
                            'title': 'Under $25, for anyone',
                            'items': ['20W+ USB-C charger', 'Rechargeable book light', 'Smart plug'],
                            'reveal_at': ['charger', 'book', 'smart'],
                            'hold': 1.6}],
        'hashtags': ['secretsanta', 'giftideas', 'techgifts'],
        'tags': ['secret santa gift ideas under 25', 'secret santa gifts', 'tech gifts under 25'],
        'question': 'Do you know who you drew yet?',
        'affiliate': {'product_name': '30W USB-C PD GaN charger', 'search_term': '30w usb c charger'}},
    {   'slug': 'secret_santa_by_type',
        'series': 'Before you buy',
        'format': 'under_budget',
        'hook_pattern': 'one_spec',
        'two_part': {'id': 'secretsanta', 'part': 2},
        'title': 'Secret Santa under $25: match the gift to one thing you know',
        'hook_text': 'Secret Santa: one clue, one gift',
        'hook_emph': 'one clue',
        'script': 'If you know one thing about your Secret Santa, a twenty-five-dollar gift can feel picked for '
                  'them. Coffee drinker: a digital kitchen scale, since weighing the beans is the cheapest way '
                  'to a better cup. Commuter: a ten thousand milliamp hour power bank with USB-C, so their phone '
                  'makes it home. Always cold: a rechargeable hand warmer, which runs for hours on a charge. '
                  'Runner: a phone armband sized for their exact phone. Each one fits a habit instead of a '
                  'guess. So listen for one clue at work, because',
        'footage_queries': [   'person wrapping gift',
                               'pour over coffee',
                               'commuter on train with phone',
                               'warming cold hands',
                               'runner with phone armband',
                               'office christmas party'],
        'captions': [],
        'graphics': [   {   'type': 'checklist',
                            'at': 'coffee',
                            'title': 'One clue, one gift',
                            'items': [   'Coffee: kitchen scale',
                                         'Commuter: power bank',
                                         'Cold: hand warmer',
                                         'Runner: armband'],
                            'reveal_at': ['coffee', 'commuter', 'cold', 'runner']}],
        'hashtags': ['secretsanta', 'giftideas', 'techgifts'],
        'tags': ['secret santa gift ideas', 'secret santa gifts under 25', 'gifts for coworkers'],
        'question': "What's the one thing you know about your Secret Santa?",
        'affiliate': {   'product_name': 'USB-C power bank with PD fast charging',
                         'search_term': 'portable charger power bank'}},
    {   'slug': 'dad_3in1_charger_gift',
        'series': 'Before you buy',
        'format': 'before_you_buy',
        'hook_pattern': 'look_identical',
        'title': 'Gifts for dad: these 3-in-1 chargers look identical, only one charges his watch',
        'hook_text': '3-in-1? Check his watch',
        'hook_emph': 'his watch',
        'script': 'Two three-in-one charging stands can look identical, and only one will charge his watch. An '
                  'Apple Watch needs its own magnetic puck, so a stand with three flat Qi pads charges the phone '
                  'and earbuds, then leaves the watch dead. Galaxy and Pixel watches often need their own '
                  'chargers too. So check his phone and his watch first. For an iPhone and an Apple Watch, look '
                  'for a Qi2 stand with a built-in Apple Watch charger. For Android, many stands are made for '
                  "one brand's watch, so match the model. Get it right and it's the gift he uses every night. "
                  'Before you buy one, remember that',
        'footage_queries': [   'phone wireless charging',
                               'apple watch on wrist',
                               'nightstand phone charging',
                               'wireless earbuds case',
                               'man checking phone',
                               'wrapped christmas gifts'],
        'captions': [],
        'graphics': [   {   'type': 'versus',
                            'at': 'puck',
                            'left': ['Watch puck', 'charges it'],
                            'right': ['Three flat Qi pads', 'watch stays dead'],
                            'winner': 'left',
                            'reveal_at': ['puck', 'pads']},
                        {   'type': 'checklist',
                            'at': 'iPhone',
                            'title': 'Match his gear',
                            'items': ['iPhone: Qi2 + watch puck', 'Android: match the watch'],
                            'reveal_at': ['iPhone', 'android']}],
        'hashtags': ['giftsfordad', 'giftideas', 'techgifts'],
        'tags': ['gifts for dad', '3 in 1 charging station', 'apple watch charger stand'],
        'question': 'Which phone and watch does he use?',
        'affiliate': {   'product_name': 'Qi2 3-in-1 charging stand with Apple Watch charger',
                         'search_term': 'qi2 3 in 1 charging station apple watch'}},
    {   'slug': 'trade_in_credit_vs_cash',
        'series': 'Before you buy',
        'format': 'comparison',
        'hook_pattern': 'price_vs',
        'title': 'Phone trade-in deals: $800 in bill credits vs cash up front',
        'hook_text': '$800 trade-in? Read the terms',
        'hook_emph': '$800',
        'script': "An eight-hundred-dollar trade-in offer from a carrier usually isn't eight hundred dollars up "
                  'front. Most carrier deals pay it as monthly bill credits over twenty-four to thirty-six '
                  'months, and if you switch carriers or pay off the phone early, the remaining credits often '
                  "stop. Many also require a specific plan. A cash buyer or the phone maker's own trade-in pays "
                  'less on paper, but it pays once, with no strings. So compare the two by asking one thing: '
                  'what do I get if I leave in a year? Before you hand over your old phone this season, remember '
                  'that',
        'footage_queries': ['smartphone in hand', 'phone store', 'new phone unboxing', 'old smartphone on table', 'person using smartphone at home', 'signing contract'],
        'captions': [{'text': 'Leave early = credits stop', 'at': 'remaining'}],
        'graphics': [   {   'type': 'versus',
                            'at': 'monthly',
                            'left': ['Carrier credit', 'over 24-36 months'],
                            'right': ['Cash trade-in', 'paid once'],
                            
                            'dur': 4.5}],
        'hashtags': ['smartphone', 'blackfriday', 'techtips'],
        'tags': ['phone trade in deal', 'carrier trade in credit', 'trade in iphone'],
        'question': 'Did you trade in your last phone or sell it?'},
    {
        "slug": "screen_cleaner_vs_water",
        "series": "Before you buy",
        "format": "comparison",
        "title": "Glass cleaner vs water: what's actually safe for your laptop screen",
        "hook_text": "Glass cleaner vs your screen",
        "hook_emph": "Glass cleaner",
        "script": (
            "Glass cleaner and a paper towel can slowly ruin your screen, even though they feel like the obvious "
            "choice. Most laptop and phone screens have a thin coating that resists fingerprints, and ammonia-based "
            "cleaners wear it down over time. Paper towels are slightly abrasive, so they leave fine scratches you "
            "only notice in bright light. The safe way is simple: a microfiber cloth, lightly dampened with plain "
            "water, wiped gently. Spray the cloth, never the screen, so nothing seeps into the edges. Because"
        ),
        "footage_queries": ["cleaning screen", "cleaning laptop screen cloth", "glass cleaner spray bottle",
                            "paper towel", "microfiber cloth closeup", "laptop screen closeup",
                            "spray bottle"],
        "captions": [{"text": "Spray the cloth, never the screen", "at": "spray"}],
        "graphics": [
            {"type": "checklist", "at": "coating", "title": "What goes wrong", "style": "avoid",
             "items": ["Ammonia strips coating", "Paper towels scratch"],
             "reveal_at": ["ammonia", "paper"], "hold": 4.6},
            {"type": "versus", "at": "safe", "left": ["Glass cleaner", "strips coating, scratches"],
             "right": ["Microfiber", "+ plain water, gently"], "winner": "right", "dur": 5.4},
        ],
        "hashtags": ["laptop", "cleaning", "techtips"],
        "tags": ["how to clean laptop screen", "screen cleaning", "microfiber cloth"],
        "question": "What have you been cleaning your screen with?",
        "affiliate": {"product_name": "microfiber cleaning cloths for screens", "search_term": "microfiber cleaning cloth screens"},
    },
    {   'slug': 'hand_down_phone_signout',
        'series': 'Settings worth changing',
        'format': 'before_you_buy',
        'hook_pattern': 'one_spec',
        'title': 'Handing down your old phone? Sign out first or it can lock',
        'hook_text': 'Old phone gift? Sign out first',
        'hook_emph': 'Sign out',
        'script': 'Sign out of your account first, or the person you hand your old phone to may get a locked '
                  'brick. iPhones have Activation Lock, and Android has Factory Reset Protection. Both tie the '
                  'phone to your account, even after a wipe. On iPhone, back up, then go to Settings, tap your '
                  'name, sign out, and erase all content and settings. On Android, back up, remove your Google '
                  'account under Settings, Accounts, then factory reset. Take out the SIM card or delete the '
                  'eSIM too. The whole thing takes about ten minutes, so when you upgrade this year,',
        'footage_queries': [   'old smartphone',
                               'person giving phone gift',
                               'smartphone settings screen',
                               'unboxing new smartphone',
                               'sim card tray',
                               'phone factory reset screen'],
        'captions': [],
        'graphics': [   {   'type': 'steps',
                            'at': 'back',
                            'title': 'iPhone',
                            'items': ['Back up', 'Sign out', 'Erase all content'],
                            'reveal_at': ['back', 'sign', 'erase'],
                            'hold': 1.0},
                        {   'type': 'steps',
                            'at': 'google',
                            'title': 'Android',
                            'items': ['Remove Google account', 'Factory reset'],
                            'reveal_at': ['google', 'factory']}],
        'hashtags': ['iphone', 'android', 'techtips'],
        'tags': ['reset phone before giving away', 'factory reset protection', 'activation lock'],
        'question': "Who's getting your old phone this year?"},
    {
        "slug": "browser_passwords_vs_manager",
        "series": "Security in 30 seconds",
        "format": "comparison",
        "title": "Browser passwords vs a password manager: is the built-in one enough?",
        "hook_text": "Your password saver is enough",
        "hook_emph": "password saver",
        "script": (
            "Is the password saver in your browser actually good enough? For most people, yes. The ones built "
            "into your iPhone, your Android phone or your browser now create strong passwords, sync across your "
            "devices, and warn you about leaks. A dedicated manager makes sense if you mix ecosystems, like an "
            "iPhone with a Windows PC, share logins with family, or want to store things like recovery codes. But "
            "the real danger isn't picking the wrong one. It's reusing the same password. So open your saved "
            "passwords today, fix any reuse warnings starting with your email, and then ask yourself:"
        ),
        "footage_queries": ["password", "typing password on laptop", "smartphone and laptop on desk",
                            "family sharing tablet couch", "using smartphone on couch", "laptop keyboard closeup",
                            "padlock security concept"],
        "captions": [{"text": "Strong passwords, sync, leak alerts", "at": "strong"},
                     {"text": "Reused passwords are the real risk", "at": "danger"}],
        "graphics": [
            {"type": "versus", "at": "dedicated", "left": ["Built-in", "fine for most people"],
             "right": ["Manager", "iPhone + PC, sharing"], "dur": 8.4},
            {"type": "checklist", "at": "open", "title": "Do this today",
             "items": ["Open saved passwords", "Fix reuse warnings", "Start with your email"],
             "reveal_at": ["open", "reuse", "email"]},
        ],
        "hashtags": ["cybersecurity", "passwords", "techtips"],
        "tags": ["password manager", "browser password manager", "password security"],
        "question": "Built-in password saver or a dedicated manager?",
    },
    {
        "slug": "five_g_battery_drain",
        "series": "Settings worth changing",
        "format": "did_you_know",
        "title": "Why 5G might be draining your battery faster than 4G",
        "hook_text": "Weak 5G drains your battery",
        "hook_emph": "5G",
        "script": (
            "5G could be the reason your battery dies faster than it used to. When the 5G signal is "
            "weak, your phone keeps hunting between 5G and 4G, and that burns power. For texting, maps and music, "
            "you usually can't tell the difference anyway. On iPhone, go to Settings, Cellular, Cellular Data "
            "Options, Voice and Data, and pick 5G Auto. On Android, open your network settings, find preferred "
            "network type, and choose LTE if 5G is spotty where you live. Try it for a week and watch your "
            "battery screen, because"
        ),
        "footage_queries": ["phone battery", "low battery phone screen", "phone signal bars city",
                            "person using phone on street", "texting on phone", "listening to music on phone",
                            "phone settings menu scrolling"],
        "captions": [{"text": "Try it for a week", "at": "try"}],
        "graphics": [
            # Apple: 5G Auto switches to LTE when 5G wouldn't be noticeably faster
            {"type": "versus", "at": "weak", "left": ["Always 5G", "hunts on a weak signal"],
             "right": ["5G Auto", "5G only when it helps"], "winner": "right", "dur": 4.4},
            {"type": "steps", "at": "iphone", "title": "iPhone",
             "items": ["Settings", "Cellular", "Cellular Data Options", "Voice & Data: 5G Auto"],
             "reveal_at": ["settings", "cellular", "options", "voice"]},
            {"type": "steps", "at": "android", "title": "Android",
             "items": ["Network settings", "Preferred network type", "LTE if 5G is spotty"],
             "reveal_at": ["network", "preferred", "lte"]},
        ],
        "hashtags": ["iphone", "battery", "techtips"],
        "tags": ["5g battery drain", "iphone battery tips", "5g auto"],
        "question": "Do you keep 5G on, or Auto?",
    },
    {
        "slug": "search_with_your_camera",
        "series": "Settings worth changing",
        "format": "comparison",
        "title": "Stop typing what you're trying to find. Search with your camera instead",
        "hook_text": "Your camera is a search bar",
        "hook_emph": "camera",
        "script": (
            "Stop trying to describe things in a search bar. Your phone can search with a photo instead. On "
            "iPhone, open any photo and tap the info button with the little sparkles, or touch and hold something "
            "in the picture. It identifies plants, products, landmarks and even dog breeds. On Android, open "
            "Google Lens from the camera or the search bar, and on many phones you can circle anything on screen "
            "to search it. It's the fastest way to find where to buy something you saw, or to translate a sign. "
            "So next time you can't find the right words,"
        ),
        "footage_queries": ["phone camera", "phone camera scanning object", "person taking photo of plant",
                            "landmark tourist photo", "dog breed", "street sign foreign city",
                            "phone identifying product photo"],
        "captions": [{"text": "iPhone: tap the info button", "at": "tap"},
                     {"text": "Fastest way to shop or translate", "at": "fastest"}],
        "graphics": [
            {"type": "versus", "at": "photo", "left": ["Typing", "guessing the right words"],
             "right": ["Camera", "point and tap"], "winner": "right", "dur": 4.0},
            {"type": "checklist", "at": "identifies", "title": "It identifies",
             "items": ["Plants", "Products", "Landmarks + dog breeds"],
             "reveal_at": ["plants", "products", "landmarks"]},
            {"type": "steps", "at": "android", "title": "Android",
             "items": ["Open Google Lens", "Or circle to search"], "reveal_at": ["google", "circle"]},
        ],
        "hashtags": ["iphone", "android", "techtips"],
        "tags": ["google lens", "visual look up", "circle to search"],
        "question": "Have you tried searching with a photo yet?",
    },
]
