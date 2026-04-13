# Golf Rules Test Cases

This document contains 40 golf rules questions categorized by difficulty level for testing a golf rules bot. Questions are sourced from golf forums, USGA quizzes, and community discussions.

## Easy Golf Rules Questions (10)

### test001
- **id**: test001
- **difficulty**: easy
- **category**: bunker
- **question**: If you touch the sand in a bunker with your club before making a stroke, what is the penalty?
- **source URL**: https://onlineexammaker.com/kb/20-golf-rules-quiz-questions-and-answers/
- **top_comment**: One penalty stroke is added according to Rule 12.2b for improving conditions affecting the stroke.
- **ground_truth**: **Rule 12.2b(1)** - A player must not deliberately touch sand in a bunker with a club in the area right in front of or behind the ball, during a practice swing, or during the backswing. **Penalty**: General penalty (2 strokes in stroke play, loss of hole in match play). **Ruling**: If you touch the sand with your club before making a stroke, you incur the general penalty - add 2 penalty strokes to your score and play the ball as it lies. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-12
- **format**: stroke

### test002
- **id**: test002
- **difficulty**: easy
- **category**: ball_marking
- **question**: How should you mark your ball on the putting green before lifting it?
- **source URL**: https://www.usga.org/content/usga/home-page/rules/rules-2019/players-edition/rule-14.html
- **top_comment**: You must mark the spot by placing a ball-marker immediately behind or next to the ball or by placing a club on the ground immediately behind or next to the ball.
- **ground_truth**: **Rule 14.1a** - Before lifting a ball that must be replaced on its original spot, mark the spot by: (1) placing a ball-marker right behind or right next to the ball, or (2) holding a club on the ground right behind or right next to the ball. **Ruling**: Mark your ball before lifting using either method. Remove the ball-marker before making your next stroke or incur a 1-stroke penalty. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-14
- **format**: stroke

### test003
- **id**: test003
- **difficulty**: easy
- **category**: equipment
- **question**: Who is allowed to drop your ball when taking relief?
- **source URL**: https://www.randa.org/en/rog/the-rules-of-golf/rule-14
- **top_comment**: The ball must be dropped only by the player. Neither the player's caddie nor anyone else may do so.
- **ground_truth**: **Rule 14.3b(1)** - The ball must be dropped only by the player. Neither the player's caddie nor anyone else may do so. **Ruling**: Only you are allowed to drop your ball when taking relief. Your caddie or anyone else cannot drop it for you (except for players with disabilities under specific modifications). **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-14
- **format**: stroke

### test004
- **id**: test004
- **difficulty**: easy
- **category**: provisional
- **question**: When can you play a provisional ball?
- **source URL**: https://sites.google.com/site/kitchenergaffers/rules-guidelines/provisional-ball
- **top_comment**: A provisional ball can be played if a ball might be lost or if it might be out of bounds.
- **ground_truth**: **Rule 18.3a** - If a ball might be lost outside a penalty area or might be out of bounds, to save time the player may play another ball provisionally under penalty of stroke and distance. **Ruling**: You can play a provisional ball when your original ball might be lost outside a penalty area or might be out of bounds. You must announce it as a "provisional" before playing. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-18
- **format**: stroke

### test005
- **id**: test005
- **difficulty**: easy
- **category**: embedded
- **question**: Where on the course can you get free relief from an embedded ball?
- **source URL**: https://www.golfmonthly.com/videos/rules/rules-of-golf-plugged-lie
- **top_comment**: Unless you are in a bunker or penalty area, you get relief without penalty from an embedded ball in the general area.
- **ground_truth**: **Rule 16.3a/16.3b** - Relief is allowed only when a player's ball is embedded in the general area. No relief if the ball is embedded anywhere except in the general area (no relief in bunkers or penalty areas). Exception: no relief if embedded in sand that is not cut to fairway height or less. **Ruling**: You get free relief from an embedded ball only in the general area (fairway/rough), not in bunkers or penalty areas. Drop within one club-length behind where embedded, no closer to hole. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-16
- **format**: stroke

### test006
- **id**: test006
- **difficulty**: easy
- **category**: match_play
- **question**: In match play, if your ball in motion accidentally hits your opponent, what is the penalty?
- **source URL**: https://www.glenelggolf.com/cms/rules/a-guide-to-the-rules-of-match-play/
- **top_comment**: There is no penalty to either player, and the ball will normally be played as it lies.
- **ground_truth**: **Rule 11.1a** - There is no penalty to any player when a ball in motion accidentally hits an opponent, their caddie, or equipment. **Ruling**: In match play, if your ball accidentally hits your opponent, there is no penalty to either player. Play the ball from where it comes to rest. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-11
- **format**: match

### test007
- **id**: test007
- **difficulty**: easy
- **category**: caddie
- **question**: Can your caddie give you advice during a round?
- **source URL**: https://www.randa.org/en/rog/the-rules-of-golf/rule-10
- **top_comment**: Yes, a player may seek advice from their caddie during a match.
- **ground_truth**: **Rule 10.2a** - During play, a player must not ask anyone for advice, other than the player's caddie. **Ruling**: Yes, your caddie can give you advice during a round. Your caddie is the only person you may ask for advice on strategy, club selection, line of play, and other golf decisions during play. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-10
- **format**: stroke

### test008
- **id**: test008
- **difficulty**: easy
- **category**: water_hazard
- **question**: If a pond has overflowed beyond its marked boundaries, what is the overflow area considered?
- **source URL**: https://onlineexammaker.com/kb/20-golf-rules-quiz-questions-and-answers/
- **top_comment**: The overflow that is outside the margin of the hazard is casual water.
- **ground_truth**: **Definitions - Temporary Water/Penalty Area** - Temporary Water is any temporary accumulation of water on the surface of the ground (such as puddles from rain or irrigation or an overflow from a body of water). However, a penalty area includes any body of water on the course, whether or not marked by the Committee. **Ruling**: Water that overflows beyond the marked boundaries of a penalty area is generally considered temporary water, allowing free relief under Rule 16.1. However, if the overflow is clearly part of the same body of water, it may still be considered part of the penalty area. **Source**: https://www.usga.org/content/usga/home-page/rules/rules-2019/committee-procedures/definitions.html
- **format**: stroke

### test009
- **id**: test009
- **difficulty**: easy
- **category**: unplayable
- **question**: Who determines if a ball is unplayable?
- **source URL**: https://www.mygolfinstructor.com/instruction/rules-of-golf/unplayable-lie/
- **top_comment**: You are the sole judge of whether your ball is unplayable.
- **ground_truth**: **Rule 19.1** - A player is the only person who may decide to treat their ball as unplayable by taking penalty relief under Rule 19.2 or 19.3. **Ruling**: You are the sole judge of whether your ball is unplayable. No one else (referee, opponent, fellow competitor) can make this decision for you. You can declare your ball unplayable anywhere on the course except in a penalty area. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-19
- **format**: stroke

### test010
- **id**: test010
- **difficulty**: easy
- **category**: match_play
- **question**: In match play, if your opponent deliberately moves your ball marker, what is the penalty?
- **source URL**: https://www.glenelggolf.com/cms/rules/a-guide-to-the-rules-of-match-play/
- **top_comment**: The opponent incurs a one penalty stroke and the marker must be replaced.
- **ground_truth**: **Rule 9.5** - When an opponent (or their caddie) deliberately lifts, touches, or moves your ball or ball-marker on the putting green, they incur one penalty stroke. The ball/marker must be restored to its original position. **Ruling**: Your opponent gets 1 penalty stroke in match play for deliberately moving your ball marker. The marker must be replaced in its original position. Exceptions: no penalty if done as a concession or at your request. **Source**: https://www.randa.org/en/players-rule-finder/players-rule-finder/putting-green/ball-or-ball-marker-moved-deliberately-by-opponent-in-match-play
- **format**: match

## Medium Golf Rules Questions (10)

### test011
- **id**: test011
- **difficulty**: medium
- **category**: GUR
- **question**: Your ball lies in a bunker that has been marked as GUR (Ground Under Repair). Where must you drop when taking full relief?
- **source URL**: https://forums.golfmonthly.com/threads/bunker-gur-where-to-drop.14609/
- **top_comment**: When taking full relief from a bunker that is GUR, you must drop in the general area outside the bunker at the nearest point of relief.
- **ground_truth**: **Rule 16.1b** - When an entire bunker is marked as ground under repair, it's treated as part of the general area. Find the nearest point of complete relief in the general area (outside the bunker), then drop within one club-length of that point, no closer to hole. **Ruling**: When taking relief from a bunker marked as GUR, you get free relief outside the bunker. Find nearest point of complete relief in general area, drop within one club-length, not closer to hole. **Source**: https://www.randa.org/en/players-rule-finder/players-rule-finder/bunker/ground-under-repair-animal-hole-or-temporary-water/relief-when-entire-bunker-is-defined-as-Ground-Under-Repair
- **format**: stroke

### test012
- **id**: test012
- **difficulty**: medium
- **category**: provisional
- **question**: You play a provisional ball, then find your original ball which is clearly unplayable. Can you abandon the original and continue with the provisional?
- **source URL**: https://www.nationalclubgolfer.com/rules/unplayable-ball-can-i-play-my-provisional-ball-instead/
- **top_comment**: No, the provisional must be abandoned when the original ball is found. You must take unplayable ball relief from where the original ball lies.
- **ground_truth**: **Rule 18.3c(3)** - When the original ball is found on the course outside a penalty area before the three-minute search time ends, the provisional ball must be abandoned. **Ruling**: No, you cannot continue with the provisional ball once your original is found. You must abandon the provisional and either play the original as it lies or declare it unplayable under Rule 19, taking the appropriate relief from the original ball's location. **Source**: https://www.randa.org/en/players-rule-finder/players-rule-finder/general-area/provisional-ball-when-provisional-ball-becomes-abandoned
- **format**: stroke

### test013
- **id**: test013
- **difficulty**: medium
- **category**: penalty_area
- **question**: Your ball crosses a red penalty area but then continues out of bounds. What are your relief options?
- **source URL**: https://forums.golfwrx.com/topic/1892960-ball-that-crosses-a-red-penalty-area-but-then-continues-ob/
- **top_comment**: Since the ball is OB, you must proceed under stroke and distance. The crossing of the penalty area is irrelevant.
- **ground_truth**: **Rule 18.1/18.2** - When a ball is out of bounds, the player must take stroke-and-distance relief by adding one penalty stroke and playing from where the previous stroke was made. **Ruling**: Since your ball is out of bounds, you must use stroke-and-distance relief (1 penalty stroke + replay from previous spot). The fact that it crossed a penalty area first is irrelevant - out of bounds takes precedence. You cannot use penalty area relief options. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-18
- **format**: stroke

### test014
- **id**: test014
- **difficulty**: medium
- **category**: obstruction
- **question**: Your ball is in a bunker resting on a concrete drainage grate. What relief do you get?
- **source URL**: https://thegolfbusiness.co.uk/2011/12/the-rules-of-golf-surrounding-bunkers/
- **top_comment**: You can take relief from the immovable obstruction, but you must drop in the bunker at the nearest point of relief.
- **ground_truth**: **Rule 16.1c** - When your ball is in a bunker with interference from an immovable obstruction (like a concrete drainage grate), you have two options: (1) Free relief within the bunker - find nearest point of complete relief in the bunker, drop within one club-length, no closer to hole. If no complete relief available in bunker, use point of maximum available relief as reference point. (2) Penalty relief outside bunker - for 1 penalty stroke, use back-on-the-line relief dropping outside bunker. **Ruling**: Take free relief in the bunker if possible, or 1-stroke penalty relief outside the bunker if needed. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-16
- **format**: stroke

### test015
- **id**: test015
- **difficulty**: medium
- **category**: match_play
- **question**: In match play, your ball overhangs the hole. Your opponent immediately concedes the putt and picks up your ball. What happens?
- **source URL**: https://www.wmga.com/wp-content/uploads/2024/02/Match-Play-Rules-and-Reminders.pdf
- **top_comment**: The putt is considered holed. A concession cannot be refused or withdrawn.
- **ground_truth**: **Rule 3.2b(1)** - In match play, your opponent may concede your next stroke at any time before you make it. Once a concession is clearly communicated, you have completed the hole with a score that includes the conceded stroke, and the ball may be removed by anyone. **Ruling**: The putt is considered holed with your previous stroke. A concession is final and cannot be declined or withdrawn. Your opponent can pick up your ball after conceding. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-3
- **format**: match

### test016
- **id**: test016
- **difficulty**: medium
- **category**: embedded
- **question**: Your ball is embedded in the ground because someone stepped on it, not from your shot. Do you get free relief?
- **source URL**: https://www.golfdigest.com/story/rules-of-golf-most-misunderstood-rules-embedded-ball-bunker-penalty-area-out-of-bounds
- **top_comment**: No, for embedded ball relief, the ball must be in your own pitch mark from your previous stroke.
- **ground_truth**: **Rule 16.3a** - A ball is embedded only if it is in its own pitch-mark made as a result of the player's previous stroke and part of the ball is below the level of the ground. **Ruling**: No, you do not get free relief. The ball must be embedded from your own shot, not from being stepped on or any other cause. Play the ball as it lies or declare it unplayable under Rule 19. **Source**: https://www.randa.org/en/players-rule-finder/players-rule-finder/general-area/embedded-ball-when-free-relief-is-allowed
- **format**: stroke

### test017
- **id**: test017
- **difficulty**: medium
- **category**: dropping
- **question**: When dropping a ball for relief, how high must you drop it from?
- **source URL**: https://www.randa.org/en/rog/the-rules-of-golf/rule-14
- **top_comment**: The ball must be dropped from knee height, falling straight down without throwing, spinning or rolling.
- **ground_truth**: **Rule 14.3b** - The ball must be dropped from knee height (height of player's knee when standing) so that it falls straight down without throwing, spinning, or rolling it. **Ruling**: Drop from knee height. If the ball doesn't stay in relief area after proper drop, try again. If second drop also fails to stay in relief area, place the ball where it first touched the ground on the second drop. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-14
- **format**: stroke

### test018
- **id**: test018
- **difficulty**: medium
- **category**: match_play
- **question**: In match play, you ask your opponent for advice about club selection. Your opponent tells you what club they used. What is the penalty?
- **source URL**: https://www.randa.org/en/rog/the-rules-of-golf/rule-10
- **top_comment**: Both players get the general penalty (loss of hole) - you for asking for advice and your opponent for giving it.
- **ground_truth**: **Rule 10.2a/10.2b** - Players must not ask for or give advice, except to/from their own caddie. Advice includes information intended to influence club selection or how to play. **Ruling**: Both players lose the hole - you for asking for advice and your opponent for giving it. The general penalty in match play is loss of hole for each player who breached the rule. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-10
- **format**: match

### test019
- **id**: test019
- **difficulty**: medium
- **category**: bunker
- **question**: Can you remove a loose impediment (like a leaf) from a bunker if it's not near your ball?
- **source URL**: https://onlineexammaker.com/kb/20-golf-rules-quiz-questions-and-answers/
- **top_comment**: No, Rule 12.2a prohibits removing loose impediments in a bunker regardless of location.
- **ground_truth**: **Rule 15.1a** (Updated 2019) - You may remove loose impediments and movable obstructions anywhere on or off the course, including in bunkers, even when your ball also lies in the bunker. **Ruling**: Yes, you can remove loose impediments like leaves from anywhere in a bunker without penalty. This was a major rule change in 2019. The challenge is playing from sand, not playing around debris. If your ball moves while removing the impediment, replace it. **Source**: https://www.usga.org/content/usga/home-page/rules-hub/rules-modernization/major-changes/moving-or-touching-loose-impediments-or-sand-in-a-bunker.html
- **format**: stroke

### test020
- **id**: test020
- **difficulty**: medium
- **category**: relief
- **question**: You declare your ball unplayable and pick it up, then realize you were entitled to free relief. Can you change your decision?
- **source URL**: https://www.golfdigest.com/story/rules-of-golf-review-unplayable-lie-picking-up-ball-changing-mind
- **top_comment**: Yes, as long as you haven't put a ball in play, you can still take the free relief.
- **ground_truth**: **Rule 14.2/19.1** - When a ball is lifted to take relief under a rule, you don't need to mark it. If you haven't made a stroke at a replacement ball, you can change your relief option. **Ruling**: Yes, you can change your decision as long as you haven't put another ball in play by making a stroke. Replace the original ball and take the appropriate free relief instead of the unplayable ball penalty relief. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-14
- **format**: stroke

## Hard Golf Rules Questions (10)

### test021
- **id**: test021
- **difficulty**: hard
- **category**: penalty_area
- **question**: Your ball travels over a red penalty area (water), lands in someone's yard (OB), then rolls back into the water. What are your relief options?
- **source URL**: https://forums.golfwrx.com/topic/1939579-ball-travels-over-penalty-area-water-and-lands-in-a-yard-ob-only-to-fall-back-into-the-water/
- **top_comment**: You proceed under penalty area relief using the point where the ball last crossed the penalty area margin before coming to rest in the penalty area, not where it went OB.
- **ground_truth**: **Rule 17.1d** - The reference point for penalty area relief is where the ball last crossed the edge of the penalty area before coming to rest in the penalty area, not where it went out of bounds first. **Ruling**: Use penalty area relief options (stroke-and-distance, back-on-the-line, or lateral relief for red penalty area) with reference point being where the ball last crossed the penalty area margin before coming to rest in the water, regardless of the out-of-bounds excursion. **Source**: https://www.usga.org/content/usga/home-page/rules-hub/topics/penalty-areas.html
- **format**: stroke

### test022
- **id**: test022
- **difficulty**: hard
- **category**: match_play
- **question**: In match play, your opponent's ball overhangs the hole. You immediately pick it up thinking it's good. Your opponent hadn't conceded. What happens?
- **source URL**: https://www.glenelggolf.com/cms/rules/a-guide-to-the-rules-of-golf/
- **top_comment**: If the ball would have fallen in during the reasonable time to reach the hole plus 10 seconds, it's treated as holed with the previous stroke. You get the general penalty.
- **ground_truth**: **Rule 13.3b** - If a ball overhanging the hole is deliberately lifted by the opponent before the 10-second waiting period ends, the player's ball is treated as holed with the previous stroke and there is no penalty to the opponent. **Ruling**: Your opponent's ball is treated as holed with their previous stroke. You get no penalty in match play because the opponent benefits from your action. The ball must be replaced on the lip if it would not have fallen in. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-13
- **format**: match

### test023
- **id**: test023
- **difficulty**: hard
- **category**: GUR
- **question**: Your ball is in a bunker marked as GUR, but there's an area of good sand nearby in the same bunker. Can you drop in the good sand?
- **source URL**: https://forums.golfwrx.com/topic/1869430-bunkers-out-of-playgur/
- **top_comment**: No, when the entire bunker is marked as GUR, you cannot get relief within the bunker. You must take full relief outside the bunker or play as it lies.
- **ground_truth**: **Rule 16.1b** - When an entire bunker is marked as GUR, it is treated as part of the general area. You must take relief outside the bunker by finding the nearest point of complete relief in the general area, then drop within one club-length, not nearer the hole. **Ruling**: No, you cannot drop in the good sand within the bunker. You must take free relief outside the bunker or play the ball as it lies. **Source**: https://www.randa.org/en/players-rule-finder/players-rule-finder/bunker/ground-under-repair-animal-hole-or-temporary-water/relief-when-entire-bunker-is-defined-as-Ground-Under-Repair
- **format**: stroke

### test024
- **id**: test024
- **difficulty**: hard
- **category**: ball_in_motion
- **question**: Your ball is rolling on the green when your opponent, not knowing you had played, walks into its path. The ball hits their foot and stops near the hole. What happens in match play?
- **source URL**: https://www.usga.org/content/usga/home-page/rules-hub/a-short-course-on-the-rules/quiz-questions-for-ball-in-motion.html
- **top_comment**: No penalty to either player. The ball is played as it lies since the deflection by the opponent was accidental.
- **ground_truth**: **Rule 11.1a** - When a ball in motion is accidentally deflected or stopped by an opponent, opponent's caddie, or opponent's equipment in match play, there is no penalty to any player. **Ruling**: No penalty to either player. Play the ball as it lies from where it stops near the hole. The accidental deflection is treated as a rub of the green. **Source**: https://www.randa.org/en/rog/the-rules-of-golf/rule-11
- **format**: match

### test025
- **id**: test025
- **difficulty**: hard
- **category**: equipment
- **question**: During your round, your driver shaft cracks (not from abuse). Can you replace it with a different driver you have in your car?
- **source URL**: https://ilovegolfwhen.com/rules-of-golf-2026/
- **top_comment**: Yes, under the 2026 rules changes, you can replace a damaged club during the round if it wasn't damaged from abuse, using parts you or your group are carrying.
- **ground_truth**: **Rule 4.1a(2)** - You may replace a club damaged during the round (not from abuse) but cannot obtain it from outside the competition area. **Ruling**: No, you cannot get a replacement club from your car during the round. You can only replace with clubs you or someone in your group are carrying. Under Model Local Rule G-9 (if in effect), replacement must fill the same gap in your set. **Source**: https://www.usga.org/content/usga/home-page/rules-hub/rules-modernization/major-changes/adding-clubs-to-replace-a-club-damaged-during-round.html
- **format**: stroke

### test026
- **id**: test026
- **difficulty**: hard
- **category**: pitch_mark
- **question**: Your ball lies in an unrepaired pitch mark that was clearly made by another player's ball. Can you take free relief?
- **source URL**: https://ilovegolfwhen.com/rules-of-golf-2026/
- **top_comment**: Yes, under the 2026 rules changes, you can take free relief from any unrepaired pitch mark below ground level, not just ones your ball created.
- **ground_truth**: 
- **format**: stroke

### test027
- **id**: test027
- **difficulty**: hard
- **category**: match_play
- **question**: In match play, you accidentally play your opponent's ball from the rough. When do you realize the mistake and what's the penalty?
- **source URL**: https://www.wmga.com/wp-content/uploads/2024/02/Match-Play-Rules-and-Reminders.pdf
- **top_comment**: You lose the hole when you make a stroke at a wrong ball, regardless of when you discover the mistake.
- **ground_truth**: 
- **format**: match

### test028
- **id**: test028
- **difficulty**: hard
- **category**: bunker
- **question**: Your ball is in a bunker on damaged artificial lining (concrete/matting). The sand doesn't completely cover the artificial surface. What relief do you get?
- **source URL**: https://forums.golfmonthly.com/threads/free-relief-from-damaged-bunker-lining.119852/
- **top_comment**: You can take relief from the immovable obstruction but must drop in the bunker. If no relief is available in the bunker, you can take penalty relief outside the bunker.
- **ground_truth**: 
- **format**: stroke

### test029
- **id**: test029
- **difficulty**: hard
- **category**: preferred_lies
- **question**: When preferred lies are in effect, how far can you move your ball under the 2026 rules?
- **source URL**: https://www.golfyack.com/spotlight/golf-rules-changes-for-2026-what-the-tours-are-actually-updating-and-why
- **top_comment**: Under 2026 rules changes, you can move your ball one scorecard length (not a full club length) when preferred lies are in effect.
- **ground_truth**: 
- **format**: stroke

### test030
- **id**: test030
- **difficulty**: hard
- **category**: OB
- **question**: Under the 2026 PGA Tour local rule changes, when does internal out of bounds apply?
- **source URL**: https://golf.com/instruction/rules/rules-changes-pga-tour-2026/
- **top_comment**: Internal OB only applies to balls struck from the tee, not from the fairway or other areas of the course.
- **ground_truth**: 
- **format**: stroke

## Adversarial Golf Rules Questions (10)

### test031
- **id**: test031
- **difficulty**: adversarial
- **category**: provisional
- **question**: You hit a provisional ball for a ball that might be lost. After a 2-minute search, you find what might be your original ball but aren't 100% sure it's yours. Should you continue with the provisional since you can't positively identify the original?
- **source URL**: https://www.randa.org/en/rog/the-rules-of-golf/rule-18
- **top_comment**: If you cannot positively identify the ball as yours, it is not your ball. You should continue with the provisional ball.
- **ground_truth**: 
- **format**: stroke

### test032
- **id**: test032
- **difficulty**: adversarial
- **category**: match_play
- **question**: In match play, you concede your opponent's 3-foot putt, but they want to putt it anyway "for practice." Can they do this?
- **source URL**: https://www.glenelggolf.com/cms/rules/a-guide-to-the-rules-of-match-play/
- **top_comment**: No, a concession cannot be refused. The hole is over and they cannot putt for practice during play of the hole.
- **ground_truth**: 
- **format**: match

### test033
- **id**: test033
- **difficulty**: adversarial
- **category**: ball_movement
- **question**: Your ball moves slightly after you address it, but you weren't sure it moved and played it from the new position. Under 2026 rules, what's the penalty?
- **source URL**: https://ilovegolfwhen.com/rules-of-golf-2026/
- **top_comment**: If you were unaware the ball might have moved, the penalty is one stroke (not two) for playing from the wrong place.
- **ground_truth**: 
- **format**: stroke

### test034
- **id**: test034
- **difficulty**: adversarial
- **category**: embedded
- **question**: Your ball is clearly embedded in the fairway, but it's embedded in sand that was scattered from a nearby bunker, not in the actual ground/turf. Do you get relief?
- **source URL**: https://www.golfdigest.com/story/rules-of-golf-most-misunderstood-rules-embedded-ball-bunker-penalty-area-out-of-bounds
- **top_comment**: No relief. The ball must be embedded in the ground itself, not in loose sand or other materials on top of the ground.
- **ground_truth**: 
- **format**: stroke

### test035
- **id**: test035
- **difficulty**: adversarial
- **category**: bunker
- **question**: Your ball is in a bunker and you want to measure the distance to the pin. Can you place your rangefinder on the sand to stabilize it while measuring?
- **source URL**: https://thegolfbusiness.co.uk/2011/12/the-rules-of-golf-surrounding-bunkers/
- **top_comment**: No, this would be testing the condition of the sand which is prohibited under Rule 12.2a.
- **ground_truth**: 
- **format**: stroke

### test036
- **id**: test036
- **difficulty**: adversarial
- **category**: match_play
- **question**: In match play, after your opponent holes out, you ask them what club they used for their approach shot. They tell you. Who gets penalized?
- **source URL**: https://www.randa.org/en/rog/the-rules-of-golf/rule-10
- **top_comment**: No one gets penalized. Information about clubs used for completed strokes can be shared; it's only advice about future strokes that's prohibited.
- **ground_truth**: 
- **format**: match

### test037
- **id**: test037
- **difficulty**: adversarial
- **category**: penalty_area
- **question**: Your ball clearly went into a water hazard, but the area isn't marked with red or yellow stakes. Can you take penalty area relief?
- **source URL**: https://forums.golfwrx.com/topic/1847515-penalty-area-boundaries/
- **top_comment**: No, an area must be properly marked to be a penalty area. Without markings, you must treat it as you find it or take unplayable ball relief.
- **ground_truth**: 
- **format**: stroke

### test038
- **id**: test038
- **difficulty**: adversarial
- **question**: You're taking relief from GUR and your ball rolls closer to the hole after dropping. Your playing partner says you must re-drop. Are they correct?
- **source URL**: https://www.usga.org/content/usga/home-page/rules/rules-2019/players-edition/rule-14.html
- **top_comment**: Not necessarily. The ball can roll closer to the hole as long as it doesn't roll outside the relief area and isn't nearer the hole than the reference point.
- **ground_truth**: 
- **format**: stroke

### test039
- **id**: test039
- **difficulty**: adversarial
- **category**: equipment
- **question**: Your caddie accidentally breaks your putter during the round (not from abuse). Can you replace it with a different putter from the pro shop?
- **source URL**: https://ilovegolfwhen.com/rules-of-golf-2026/
- **top_comment**: No, you can only replace a damaged club with one you or your group are carrying. You cannot go get a new club from the pro shop.
- **ground_truth**: 
- **format**: stroke

### test040
- **id**: test040
- **difficulty**: adversarial
- **category**: unplayable
- **question**: Your ball is in an impossible lie in the woods. You decide it's unplayable and want to go back to the tee using stroke-and-distance, but your caddie already threw a ball down for lateral relief. Must you play the dropped ball?
- **source URL**: https://www.mygolfinstructor.com/instruction/rules-of-golf/unplayable-lie/
- **top_comment**: No, as long as you haven't made a stroke at the dropped ball, you can pick it up and choose a different relief option, including stroke-and-distance.
- **ground_truth**: 
- **format**: stroke

---

*Test cases compiled from various golf rules sources including USGA quizzes, golf forums, and community discussions. Sources include Golf Monthly, GolfWRX, USGA, Golf Digest, and official R&A publications.*