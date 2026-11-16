import json, pathlib

ROOT = pathlib.Path(__file__).parent
passages=[]
questions=[]
def passage(title, text, image_index):
    passages.append(dict(title=title,text=text,source=sorted((ROOT/'image').glob('*.jpg'))[image_index].relative_to(ROOT).as_posix()))
    return len(passages)-1
def original(pid, start, rows):
    for n,line in enumerate(rows.strip().splitlines(),start):
        parts=line.split('|')
        questions.append(dict(id=f'g{n}',number=str(n),kind='original',passage=pid,q=parts[0],options=parts[1:5],answer='ABCD'.index(parts[5]),explanation=parts[6] if len(parts)>6 else 'Đối chiếu thông tin trong đoạn đọc.',note=parts[7] if len(parts)>7 else ''))
def extra(pid, rows):
    for line in rows.strip().splitlines():
        p=line.split('|')
        i=sum(q['kind']=='extra' for q in questions)+1
        questions.append(dict(id=f'e{i}',number=f'BS{i:03}',kind='extra',passage=pid,q=p[0],options=p[1:5],answer='ABCD'.index(p[5]),explanation=p[6]))

p=passage('Homestead Bakery · Receipt', '''Homestead Bakery
1199 Beacon St., Brookline, MA 02446
Open Monday to Saturday from 6 A.M. to 6 P.M.

23 AUGUST · 5:34 P.M.
RECEIPT NUMBER: 2527 · CASHIER: John Ricketts
3 French Croissant — $12.00
2 Rye Wheat Bread Loaf — $6.00
4 Honey Glazed Donut — $6.00
SALES TAX — $1.68
Order Total — $25.68

Homestead Bakery caters for large events and business meetings.
Visit www.homesteadbreads.com to tell us about your favorite Homestead Bakery product, and you could win a month's worth of breads and pastries. Bring this receipt to our newly opened Prince Street location and get 10% off your next purchase.''',9)
original(p,147,'''What is stated about Homestead Bakery?|It has more than one location.|It is open on public holidays.|It specializes in French pastries.|It is owned by Mr. Ricketts.|A|The receipt mentions the Beacon Street address and a newly opened Prince Street location.
Why are customers asked to visit the Prince Street location?|To nominate a bread or pastry|To place a catering order|To request a refund|To obtain a discount|D|Bring the receipt to Prince Street for 10% off.''')
extra(p,'''On which street is the address printed on the receipt?|Beacon Street|Prince Street|Main Street|Park Avenue|A|The printed address is 1199 Beacon St.
In which town is the bakery address?|Brookline|Roseville|Southport|Murrayville|A|The address says Brookline, MA.
Which day is outside the stated opening schedule?|Saturday|Monday|Sunday|Friday|C|It opens Monday to Saturday.
What time does the bakery open?|5 A.M.|6 A.M.|8 A.M.|9 A.M.|B|The opening time is 6 A.M.
How long is the bakery open on a scheduled day?|8 hours|10 hours|12 hours|24 hours|C|From 6 A.M. to 6 P.M. is 12 hours.
What is the receipt number?|2527|02446|1199|2568|A|RECEIPT NUMBER: 2527.
Who served as cashier?|Charles Bryant|Francis Powell|John Ricketts|Allen Timm|C|CASHIER: John Ricketts.
How many croissants were purchased?|Two|Three|Four|Six|B|The receipt lists 3 French Croissant.
How much did the rye wheat bread cost in total?|$12.00|$1.68|$25.68|$6.00|D|The bread line totals $6.00.
How many doughnuts were purchased?|Four|Three|Two|One|A|The receipt lists 4 Honey Glazed Donut.
What was the total before sales tax?|$25.68|$24.00|$23.00|$26.00|B|12 + 6 + 6 = $24.00.
What could customers win by giving product feedback?|Free parking|A month's worth of breads and pastries|A concert ticket|A cooking job|B|The invitation offers a month's worth of breads and pastries.''')

p=passage('Attention · Pet disposal bags', '''ATTENTION
For emergencies, we have some disposal bags available at the office near the entrance. If your pet has left unexpected droppings, please come to the front desk so you can take care of your pet's mess. There have been visitors in the past that took advantage of that and took more than five bags. To prevent that from happening again, we allow only one bag per pet.

Don't forget to have your pet on a leash, or you will be fined $50. This is a free public place that is visited by many guests. You are free to enjoy yourself, but any activity causing discomfort to other people is strictly prohibited.
Thank you.''',9)
original(p,149,'''Where is this notice most likely posted?|At a park|At a hotel|At an apartment|At a diner|A|A free public place for guests with pets is most consistent with a park.
Why can't people get more than one disposal bag?|The office budget is limited.|The suppliers are on strike.|Some people took more than they needed.|Some pets without leashes caused problems.|C|Previous visitors took more than five bags.|Một phần đáp án bị cắt ở mép ảnh; các phương án được khôi phục theo phần chữ còn thấy và ngữ cảnh.''')
extra(p,'''Where can visitors obtain a disposal bag?|At the office near the entrance|In the kitchen|At a garage|On the rooftop|A|The notice identifies the office near the entrance.
What are the bags intended for?|Carrying books|Cleaning up pet droppings|Wrapping bread|Collecting tickets|B|Visitors can use them to take care of their pet's mess.
Where should a visitor go after an unexpected pet mess?|The stage|The boardroom|The front desk|The helipad|C|The notice asks visitors to come to the front desk.
How many bags per pet are allowed?|Five|Three|Two|One|D|The limit is one bag per pet.
What behavior caused the bag restriction?|People took excessive bags|Pets ate bread|Guests arrived early|Staff changed jobs|A|Some visitors took more than five bags.
What must visitors use for their pets?|A uniform|A leash|A helmet|A ticket|B|Pets must be on a leash.
What is the fine for ignoring the leash rule?|$15|$25|$50|$70|C|The fine stated is $50.
What does the notice say about admission?|It costs $50|It requires membership|It is by appointment|The place is free to use|D|It describes a free public place.
Which activity is prohibited?|Anything causing discomfort to others|Walking quietly|Enjoying the place|Asking the front desk for a bag|A|Activities causing discomfort to others are prohibited.
Who is mainly addressed by this notice?|Job applicants|Visitors with pets|Board members|Restaurant suppliers|B|The instructions address people bringing pets.
Why does the notice mention many guests?|To announce a concert|To recruit staff|To emphasize consideration for other visitors|To sell admission|C|The shared public setting explains the conduct rules.
What should a guest do if a pet makes a mess?|Leave immediately without cleaning|Ask others to clean|Take five bags|Get a bag and clean up|D|The notice directs guests to obtain a bag and take care of the mess.''')

p=passage('Anna Takashi & James Rutherford · Text messages', '''7:48 P.M. — Anna Takashi: Are you here yet? There is already a huge line at the entrance. You should really hurry.
7:56 P.M. — James Rutherford: No way! The show starts at 9:00 P.M. though. I just got here, and that line really is huge. However, I can't find you among all these people.
7:59 P.M. — Anna Takashi: I'm in a red shirt next to the entrance where the washrooms are. I see you. Stay there, and I will go to you.''',8)
original(p,151,'''What is implied about Ms. Takashi?|She needs to go to the washroom.|She is lost.|She is lining up at the entrance.|She is on time for the show.|D|She is already at the venue before the 9 P.M. show.
At 7:56 P.M., what does Mr. Rutherford most likely mean when he writes, “No way!”?|He does not want to hurry.|He is surprised that people came so early for the show.|He is disappointed that he will not be able to watch the show.|He cannot locate Ms. Takashi.|B|He is surprised by the long line despite the show starting at 9 P.M.''')
extra(p,'''Who sends the first message?|Anna Takashi|James Rutherford|Wendi Davis|Amy Manning|A|Anna writes at 7:48 P.M.
When is the first message sent?|7:56 P.M.|7:48 P.M.|7:59 P.M.|9:00 P.M.|B|The first timestamp is 7:48 P.M.
What does Anna notice at the entrance?|A closed gate|An empty room|A huge line|A delivery truck|C|She says there is already a huge line.
What does Anna initially advise James to do?|Cancel the show|Buy bread|Call a caterer|Hurry|D|She writes, “You should really hurry.”
When does James say the show starts?|9:00 P.M.|7:48 P.M.|7:56 P.M.|8:00 P.M.|A|James states that the show starts at 9 P.M.
At 7:56 P.M., where is James?|Still at home|At the venue|In another city|Inside a restaurant|B|He says he has just arrived and sees the line.
What problem does James report?|He lost his ticket|He missed the show|He cannot find Anna|He forgot the date|C|He cannot find her among the people.
What color shirt is Anna wearing?|Blue|White|Black|Red|D|Anna identifies her red shirt.
Which landmark helps identify Anna's position?|The washrooms near the entrance|A rooftop pool|A bakery counter|A boardroom door|A|She is next to the entrance where the washrooms are.
Who sees the other person first in the final message?|James sees Anna|Anna sees James|Neither sees the other|A cashier sees both|B|Anna says, “I see you.”
What does Anna ask James to do at 7:59 P.M.?|Go home|Join another line|Stay where he is|Enter the washroom|C|She writes, “Stay there.”
How long before the show is Anna's final message sent?|30 minutes|45 minutes|2 hours|61 minutes|D|From 7:59 P.M. to 9 P.M. is 61 minutes.''')

p=passage('Victoria Public Library · Changes to library hours', '''To: All Members
From: Victoria Public Library <info@vpl.org>
Date: Friday, August 28
Subject: Changes to Library Hours

As part of the Energy Conservation Movement in the Victoria community, we have been evaluating our energy use in great detail. — [1] —. We took these measures to see how often each area of our facility is frequented during the morning, afternoon, and evening. — [2] —. In light of this, we are going to limit access to these areas. That way, we can shut off all lights, computers, and heating/cooling to these areas, saving energy and related costs. — [3] —.

New Department Hours:
Archives: 9–10 A.M., Monday–Wednesday
Government Documents: 9–10 A.M., Mondays only
Special Collections: 8 A.M.–12 P.M., Fridays & Saturdays only
Children's Books: 11 A.M.–5 P.M., Monday–Friday and 8 A.M.–3 P.M., Saturday

If you have any questions about these new hours of availability, we welcome your calls and e-mails. — [4] —.
Sincerely,
The Victoria Public Library Staff''',8)
original(p,153,'''Why did the Victoria Public Library keep track of facility visitors?|To gauge whether membership fees should increase|To decide if the library was a good use of public funds|To determine if it could afford to renovate the lobby|To discover how each area was being used by patrons|D|The library tracked how often each area was frequented.
When can a child find a book appropriate for his reading level?|At 8 A.M. on Friday|At 5 P.M. on Saturday|At 3 P.M. on Tuesday|At 11 A.M. on Sunday|C|Children's Books is open 11 A.M.–5 P.M. on Tuesday.
In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong? “What we discovered is that some areas are barely frequented at all.”|[1]|[2]|[3]|[4]|B|The finding follows the description of measuring use and precedes the decision to limit access.''')
extra(p,'''Who receives the library e-mail?|All members|Only children|Job applicants|Suppliers|A|The To line says All Members.
What is the date of the e-mail?|May 28|Friday, August 28|March 11|April 13|B|The header gives Friday, August 28.
What community initiative motivates the changes?|A concert series|A sales project|The Energy Conservation Movement|An overseas tour|C|The opening sentence names the movement.
What has the library evaluated in detail?|Ticket sales|Staff uniforms|Catering prices|Its energy use|D|The library has evaluated its energy use.
Which equipment can be turned off in restricted areas?|Lights, computers, and heating/cooling|Ovens only|Cars only|Telephones only|A|These three categories are listed in the e-mail.
When are Archives open?|8 A.M.–noon Friday|9–10 A.M., Monday–Wednesday|11 A.M.–5 P.M. daily|Only Sunday evenings|B|The new Archives schedule is 9–10 A.M., Monday–Wednesday.
On which day can members access Government Documents?|Tuesday|Saturday|Monday|Friday|C|Government Documents is open Mondays only.
When do Special Collections close on Friday?|3 P.M.|5 P.M.|10 A.M.|12 P.M.|D|Special Collections runs from 8 A.M. to noon.
Which department is available at 8:30 A.M. on Saturday?|Special Collections|Archives|Government Documents|No department listed|A|Special Collections is open 8 A.M.–noon on Saturday.
How many hours is Children's Books open on Saturday?|Five|Seven|Six|Eight|B|8 A.M. to 3 P.M. is seven hours.
Which contact methods are welcomed for questions?|Fax only|In-person only|Calls and e-mails|Postal mail only|C|The closing welcomes calls and e-mails.
What is an intended result of limiting access?|Longer opening hours everywhere|Higher membership fees|More catering orders|Lower energy use and related costs|D|The e-mail explicitly aims to save energy and related costs.''')

p=passage('Vermont Institute of Technology · Refresh your Skills', '''Vermont Institute of Technology
Refresh your Skills

Technology seems to change overnight these days. If you are like the other millions of Americans who change employment once every 5 years, then you may find yourself struggling to tackle the technology encountered at your newest place of employment. If this describes you, then enroll in the Vermont Institute of Technology's (VIT), “Refresh your Skills” course today!

We have classes on the software found in every major industry: food and beverage service, education, accounting, marketing, and many more. A comprehensive list of refresher course topics can be found at our Web site at www.vit.edu/refresh/course_catalogue.

The enrollment for the summer period ends on May 1, so visit our Web site or call or visit our Registration Department at 552-3342 (3342 Main St.) sooner rather than later!''',7)
original(p,156,'''What is a common struggle for American workers?|Learning new software tools|Maintaining work and life balance|Complying with safety regulations|Wearing work attire|A|The advertisement describes difficulty with technology at a new workplace.
What is NOT indicated as a way to register at VIT?|Making a telephone call|Composing an e-mail|Referring to a Web site|Taking a campus tour|B|The notice mentions the Web site and calling or visiting the Registration Department; it does not mention e-mail.|Phương án D được chép nguyên từ ảnh; “campus tour” cũng không được nêu rõ là cách đăng ký. Câu gốc có điểm mơ hồ, đáp án B theo ghi chú trên ảnh.''')
extra(p,'''What is the advertised institution?|Vermont Institute of Technology|Victoria Public Library|Homestead Bakery|Business Builders Club|A|The heading names Vermont Institute of Technology.
What is the course called?|Working Together|Refresh your Skills|Creative Marketing Ideas|Cost Estimate|B|The course title is “Refresh your Skills.”
According to the advertisement, how often do many Americans change employment?|Every year|Every ten years|Once every five years|Every month|C|The text says once every 5 years.
Who would most benefit from the course?|People seeking pet supplies|Concert conductors|Bakery owners only|Workers facing unfamiliar workplace technology|D|The course addresses technology encountered at a new job.
Which industry is explicitly listed?|Food and beverage service|Aerospace engineering|Mining|Shipbuilding|A|Food and beverage service appears in the list.
Which other field is explicitly mentioned?|Astronomy|Accounting|Forestry|Fashion design|B|Accounting is one of the examples.
Where is the full topic list available?|On the receipt|In an attached form|On the VIT Web site|At the concert entrance|C|The advertisement directs readers to its Web site.
When does summer enrollment end?|March 11|April 13|May 8|May 1|D|The enrollment deadline is May 1.
What is the Registration Department's phone number?|552-3342|555-4059|389-1289|1-800-365-4856|A|The listed number is 552-3342.
Where is the Registration Department located?|1199 Beacon St.|3342 Main St.|Prince Street|Park Avenue|B|The address in parentheses is 3342 Main St.
Which field in the advertisement concerns teaching and learning?|Marketing|Accounting|Education|Food service|C|Education is explicitly listed.
What does “sooner rather than later” encourage readers to do?|Wait until summer ends|Change jobs immediately|Avoid registration|Register promptly|D|The phrase urges action before the deadline.''')

p=passage('Avalon Condominiums · Property for sale', '''Property for Sale
Avalon Condominiums has newly available units for sale. Three new condominiums, including the penthouse unit, have recently become available.

Avalon is conveniently located on the corner of Park Avenue and 131st Street and is across from the downtown helipad and two 24-hour secured garages. Avalon features a concierge service for package acceptance and delivery, car services, door services, protection services and escorts 24/7/365, and more. Just down the block from Avalon Condominiums, tenants will find Legacy Square, which contains luxury shopping, two five-star restaurants, a large bodega, and several other shops. Avalon also offers a fully equipped fitness center with state-of-the-art machines and weights.

For your relaxation and entertainment, Avalon Condominiums contains a rooftop Olympic-size pool in the complex and a 12-person hot tub for year-round enjoyment. Our party room features three large screen HDTVs, a wet bar, and a fully equipped kitchen for hassle-free entertaining! Avalon Condominiums was built in the 1950s, but all of the units have been renovated to include his-and-her sinks and a two-sink kitchen, complete with an island bar. There also are hookups for a complete stereo system, HDTV, and cable Internet connections in each unit.

For more information on purchasing, financing, or showings, please contact Fantasy Real Estate at 1-800-365-4856 or visit www.fantasyreal.com. Showings are given by appointment only.''',7)
original(p,158,'''What amenity is NOT offered at Avalon Condominiums?|A garage|A swimming pool|An outdoor hot tub|A physical fitness center|A|The garages are across from Avalon; they are not listed as an Avalon amenity.
What service is close to Avalon Condominiums?|A beauty salon|A gasoline station|A helicopter airport|A luxury car dealership|C|The property is across from the downtown helipad.
The phrase “state-of-the-art” in paragraph 2, line 6, is closest in meaning to|artificial|up to date|fundamental|old-fashioned|B|State-of-the-art describes modern equipment.
Which statement is true about the complimentary services at Avalon Condominiums?|Avalon announces any guest's arrival.|Avalon holds free parties periodically.|Avalon provides ticket services.|Avalon provides security guards.|D|Protection services and escorts are offered around the clock.|Mé​p phải ảnh cắt bớt chữ của một số phương án; diễn đạt được khôi phục theo phần đọc được.''')
extra(p,'''How many condominiums have recently become available?|Three|Two|Five|Ten|A|The opening paragraph says three.
Which special unit is included among the available properties?|A basement unit|The penthouse|A detached cottage|A retail shop|B|The penthouse is specifically mentioned.
At which intersection is Avalon located?|Main and Prince|Beacon and Main|Park Avenue and 131st Street|Southport and Legacy|C|The address description names this corner.
When are the nearby secured garages open?|Weekday mornings|Evenings only|Saturdays only|24 hours|D|The text says two 24-hour secured garages.
What can the concierge accept and deliver?|Packages|Exam scores|Library books only|Construction contracts|A|Package acceptance and delivery are listed.
How frequently are protection services available?|Weekdays only|24/7/365|Only at weekends|By monthly appointment|B|The text explicitly says 24/7/365.
What shopping area is down the block?|Prince Market|Northpoint Center|Legacy Square|Southport Hall|C|Legacy Square is down the block.
How many five-star restaurants are mentioned nearby?|One|Three|Four|Two|D|Legacy Square contains two five-star restaurants.
Where is the Olympic-size pool?|On the rooftop|In a garage|Across the street|In the basement|A|The complex has a rooftop Olympic-size pool.
How many people can the hot tub accommodate?|Ten|Twelve|Twenty|Six|B|It is a 12-person hot tub.
When was Avalon built?|The 1980s|The 2000s|The 1950s|The 1920s|C|The article states it was built in the 1950s.
How are property showings arranged?|Walk in anytime|Attend a weekly open house|Call the library|By appointment only|D|The final sentence requires an appointment.''')

p=passage('Ned Flannery · Allergy instructions', '''To: All instructors
From: Ned Flannery <nflannery@leter.edu>
Date: Tuesday, March 11
Subject: Please take note!
Attached file: Allergy list.doc

Dear instructors,
I have been notified that there has been a small accident with students because of a misunderstanding regarding an attendee's allergies. One of the participants opened a granola bar, and that caused the allergic individual to pass out. — [1] —. To prevent similar accidents in the future, I will be distributing a list of allergies or special conditions and basic information about the conditions. — [2] —.

Since you will be the only official personnel in the room, it will be your job to instruct the participants. — [3] —. Please mention that we will not be responsible for any circumstances that happen if we do not know about a person's condition since we already warned everyone. — [4] —.

Thank you for your cooperation.
Ned Flannery
Media Manager, Leter Education''',6)
original(p,162,'''What is indicated about Mr. Flannery?|He has been notified of a schedule change.|He will be teaching a class next Friday.|He does not participate in the lectures.|He has plans to move to Murrayville.|C|He addresses the instructors as the only official personnel in the room.
What is indicated about the list?|It is regularly updated by Mr. Flannery.|It was written for the students to be aware of allergies.|It has the names of the students that have allergies.|It has information on basic allergies and conditions.|D|The list includes allergies or special conditions and basic information about them.
In which of the positions marked [1], [2], [3], and [4] does the following sentence best belong? “She was treated immediately, but the incident was a close call.”|[1]|[2]|[3]|[4]|A|The sentence directly follows the account of the participant passing out.''')
extra(p,'''Who receives Ned Flannery's e-mail?|All instructors|All customers|Board members|Real estate agents|A|The To line says All instructors.
What day is shown in the header?|Friday, August 28|Tuesday, March 11|Monday, May 12|Thursday, May 28|B|The header gives Tuesday, March 11.
What is the attachment called?|Registration.pdf|Cost Estimate.xls|Allergy list.doc|Meeting notes.txt|C|The attachment is Allergy list.doc.
What food item triggered the incident?|A croissant|A doughnut|A pizza|A granola bar|D|A participant opened a granola bar.
What happened to the allergic individual?|The person passed out|The person left a review|The person missed a meeting|The person received a refund|A|The e-mail says the allergic individual passed out.
What will Mr. Flannery distribute?|A menu|A list of allergies and special conditions|Concert tickets|A job application|B|He plans to distribute this list.
Why is the list being distributed?|To choose a caterer|To calculate fees|To prevent similar accidents|To sell software|C|The stated purpose is preventing similar accidents.
Who will instruct the participants?|A cashier|A concierge|A board coordinator|The instructors|D|Mr. Flannery assigns this responsibility to the instructors.
What information accompanies the conditions on the list?|Basic information about the conditions|Property prices|Employee salaries|Travel schedules|A|The e-mail expressly includes basic information.
How does Mr. Flannery describe the instructors' official presence?|They will supervise remotely|They will be the only official personnel in the room|They will not be present|They will rotate with caterers|B|This is stated in the second paragraph.
What is Mr. Flannery's job title?|Club President|HR Administrator|Media Manager|Lead Researcher|C|His signature says Media Manager.
Which organization appears in the signature?|VIT|Avalon|GB F&B|Leter Education|D|The signature identifies Leter Education.''')

p=passage('Emily Tangel · Restaurant expansion estimate', '''From: etangel@recl.com
To: ggerald@dctl.com
Date: June 7
Subject: Cost Estimate
Attachment: Gerald

Dear Ms. Gerald,
It was a pleasure to meet with you yesterday and to review your plans for enlarging your restaurant business. As discussed, our financial team has calculated an estimate, which I have attached to this e-mail.

As you'll see, your plans to enlarge the floor space around the east side patio and to incorporate a stone oven into the kitchen have been figured into our estimates. The costs have been separated into labor and materials. However, you may want to consider that we can cut costs significantly by expanding the floor space on the north side patio, which would also cut down your ongoing servicing costs.

Should you decide to select us for the contract, we can start within twelve days. Please feel free to contact me with any questions you may have. I look forward to working with you.

Sincerely,
Emily Tangel''',6)
original(p,165,'''Who most likely is Ms. Tangel?|A restaurant owner|A financial advisor|A building contractor|A hotel manager|C|She provides a construction estimate and offers to begin the contract.
What was discussed at yesterday's meeting?|Possible structural alterations|Repair for weather damage|Locations for a new restaurant|Plans for a marketing campaign|A|They reviewed enlarging the patio floor space and adding a stone oven.
What is attached in the e-mail?|Detailed floor plans|Restaurant suppliers|Receipts for kitchenware|Prices for labor|D|The attached estimate separates labor and materials.
The word “significantly” in paragraph 2, line 3, is closest in meaning to|considerably|importantly|collectively|positively|A|Here it means costs can be reduced considerably.''')
extra(p,'''Who writes the cost estimate e-mail?|Emily Tangel|Amy Zhao|Maria Lawton|Desi Dutt|A|The signature names Emily Tangel.
Who is the recipient addressed in the greeting?|Mr. Timm|Ms. Gerald|Ms. Manning|Mr. Bryant|B|The greeting is Dear Ms. Gerald.
On what date was the e-mail sent?|May 12|March 11|June 7|April 13|C|The header lists June 7.
When did the writer meet the recipient?|Last month|Two weeks ago|That morning|The previous day|D|The writer says they met yesterday.
Which business does the recipient plan to enlarge?|A restaurant|A library|A bakery chain|An insurance firm|A|The opening refers to her restaurant business.
Who calculated the estimate?|The instructors|The financial team|The club members|The concert musicians|B|The financial team calculated it.
Which patio is included in the original plan?|West side|South side|East side|Rooftop|C|The estimate includes the east side patio.
What kitchen addition is included?|A dishwasher|A refrigerator|An island sink|A stone oven|D|A stone oven is to be incorporated into the kitchen.
How are the estimated costs categorized?|Labor and materials|Food and drinks|Rent and tickets|Tax and donations|A|The costs are separated into labor and materials.
Which alternative does the writer suggest?|Using the east side only|Expanding the north side patio|Closing the kitchen|Moving to another town|B|The north side patio is proposed to reduce costs.
What additional expense could the alternative lower?|Concert admission|Registration fees|Ongoing servicing costs|Shipping insurance|C|The writer says it would reduce ongoing servicing costs.
How soon could work start if the contract is awarded?|Within two months|The next day|Within five weeks|Within twelve days|D|The final paragraph gives twelve days.''')

p=passage('Sales project team · Online chat', '''3:02 P.M. — Wendi Davis: Hi, all. Before we proceed with our new sales project, has everyone checked the information I shared yesterday?
3:04 P.M. — Anna Dubose: I checked it out and thought it was pretty good. It was simple and straightforward. However, I spotted a numerical error and fixed it.
3:08 P.M. — Francis Rivera: I reviewed it, too, and noticed that your marketing strategy was like a project proposed last year by a different team.
3:10 P.M. — Wendi Davis: Oh, really? Well, I guess we are back to square one then.
3:12 P.M. — Francis Rivera: It's okay, though. We still have a lot of time to come up with a new marketing strategy.
3:13 P.M. — Anna Dubose: Francis is right. This time, we can all contribute. Why don't we have a meeting tomorrow and brainstorm some ideas?''',5)
original(p,169,'''What was wrong with Ms. Davis's marketing strategy?|It was overshadowed by other proposals.|It was similar to another proposal.|It was not completed in time.|It did not meet the expected standards.|B|Francis says it resembles a project proposed last year by a different team.
What is indicated about the new sales project?|Ms. Dubose sent it to the members.|It isn't due any time soon.|It follows a consistent format.|It needs to be completed by an individual.|B|Francis says they still have a lot of time.
What will the writers most likely do next?|They will finish their project later than planned.|They will extend their deadline.|They will attend a meeting.|They will make corrections to their project.|C|Anna proposes meeting tomorrow to brainstorm.
At 3:10 P.M., what does Ms. Davis most likely mean when she writes, “I guess we are back to square one then”?|She needs to review the other team's marketing strategy.|She is unsure of the team members' opinions.|She wants someone else on the team to correct her work.|She needs to start from the beginning again.|D|Back to square one means starting over.''')
extra(p,'''Who starts the online discussion?|Wendi Davis|Anna Dubose|Francis Rivera|Robin Atkins|A|Wendi sends the 3:02 P.M. message.
What kind of project is the team discussing?|A property renovation|A new sales project|A library archive|A concert program|B|Wendi explicitly says new sales project.
When had Wendi shared the information?|That morning|Last week|The previous day|Last year|C|She asks about information shared yesterday.
Who found a numerical error?|Wendi Davis|Francis Rivera|James Rutherford|Anna Dubose|D|Anna reports spotting and fixing it.
How does Anna describe the information?|Simple and straightforward|Long and confusing|Incomplete and unreadable|Entirely unrelated|A|These are Anna's words.
What did Anna do about the error?|Ignored it|Fixed it|Asked a caterer|Changed the deadline|B|She says she fixed the numerical error.
Who notices the similarity to an earlier project?|Anna Dubose|Robin Atkins|Francis Rivera|Ned Flannery|C|Francis makes this observation at 3:08 P.M.
When was the similar project proposed?|Yesterday|Last month|Five years ago|Last year|D|Francis says it was proposed last year.
Who proposed the earlier project?|A different team|The cashier|The library staff|A real estate firm|A|Francis specifies a different team.
What reassures Wendi after the problem is identified?|The project is already approved|There is plenty of time|A new budget is available|A customer canceled|B|Francis says they still have a lot of time.
What is the suggested purpose of tomorrow's meeting?|To distribute bonuses|To hire instructors|To brainstorm ideas|To choose a menu|C|Anna proposes brainstorming ideas.
What does Anna emphasize about the new effort?|Only Wendi should work on it|Francis must do it alone|The team should stop|Everyone can contribute|D|Anna says they can all contribute.''')

p=passage('Jeffco Brass Community Orchestra · Anniversary', '''Don't miss out!
Mark your calendars for the fifth anniversary of the formation of the Jeffco Brass Community Orchestra. The orchestra will celebrate with a special free concert on May 6 from 7:00 to 9:30 P.M. at the Jeffco Community Center. This performance will be suitable for all lovers of music. The orchestra plans to play songs in several music genres. “Our set list is comprised of popular classical music, show tunes, and even rock and modern rap songs!” exclaimed conductor Tom Allen. For more information, visit our Web site at www.jeffcobrass.com or contact Tom Allen at t.allen@jeffcobrass.com.''',5)
original(p,173,'''What is the purpose of this notice?|To publicize an organization's yearly celebration|To request donations for a charity event|To announce when tickets will go on sale|To advertise the creation of a new music group|A|It publicizes a concert celebrating the orchestra's fifth anniversary.
What is indicated about the concert?|It is not appropriate for young children.|It will include a wide range of songs.|It will provide some food and drinks.|It will collect a free-will donation.|B|The set list includes classical music, show tunes, rock, and rap.
Why would someone contact Mr. Allen?|To reserve tickets|To request a song|To ask about details|To apply for membership|C|Tom Allen is listed as a contact for more information.''')
extra(p,'''Which organization is celebrating?|Jeffco Brass Community Orchestra|Vermont Institute of Technology|Business Builders Club|Power​mount Company|A|The notice names the orchestra.
Which anniversary is being celebrated?|The first|The fifth|The tenth|The twentieth|B|It is the fifth anniversary of formation.
On what date is the concert?|May 1|May 8|May 6|May 12|C|The concert date is May 6.
When does the concert start?|6:30 P.M.|8:30 P.M.|9:30 P.M.|7:00 P.M.|D|The time range begins at 7 P.M.
When does the concert end?|9:30 P.M.|7:00 P.M.|8:00 P.M.|10:30 P.M.|A|The stated end is 9:30 P.M.
How long is the concert scheduled to last?|One hour|Two and a half hours|Three hours|Ninety minutes|B|7 P.M. to 9:30 P.M. is two and a half hours.
Where will the concert take place?|Roseville Public Library|Legacy Square|Jeffco Community Center|Northpoint Business Center|C|The venue is Jeffco Community Center.
What is the admission price?|$10|$25|$50|Free|D|It is described as a special free concert.
Who is the conductor?|Tom Allen|Charles Bryant|Allen Timm|Francis Rivera|A|Tom Allen is identified as conductor.
Which music type is explicitly included?|Only jazz|Show tunes|Only folk music|Only country music|B|Show tunes appear in the set list.
Which modern music style is named?|Disco only|Blues only|Rap|Techno only|C|Modern rap songs are mentioned.
Where can someone find more information online?|vit.edu|pomo.com|fantasyreal.com|jeffcobrass.com|D|The notice lists www.jeffcobrass.com.''')

p=passage('Multimedia Plus · Computer-skills workshops', '''Multimedia Plus
Computer-skills Workshops for Employees

Planning on improving your computer skills for your career? Multimedia Plus will be offering reasonably priced workshops at the Northpoint Business Center (except where noted). Participation is voluntary. But Powermount Company employees will receive a $10.00 discount for each workshop.

Workshop 1 — Creative Marketing Ideas
February 23, 9:00–11:30 A.M. · Fee: $40 ($30 with discount)
Workshop 2 — Introduction to Web Site Design
March 29, 9:30 A.M.–Midday · Fee: $70 ($60 with discount)
(Workshop Location: Southport Convention Center)
Workshop 3 — Powerful Presentation Applications
April 16, 10:00 A.M.–Midday · Fee: $45 ($35 with discount)
Workshop 4 — Advanced Online Research
May 8, 10:30 A.M.–Midday · Fee: $50 ($40 with discount)

To: Francis Powell
From: Desi Dutt
Date: February 20
Re: Workshop Registration
Attachment: Form

Dear Mr. Powell,
Earlier today, I saw a notice at my office relating to the computer-skills workshops your company is holding. Please find enclosed my completed registration form. I will make an online bank transfer for the discounted fee of $60.00 once confirmation of a seat is available. I am eager to attend the March workshop. Thank you for your assistance.
Regards,
Desi Dutt''',4)
original(p,176,'''For which company's employees is the notice most likely intended?|The Southport Convention Center|Multimedia Plus|The Powermount Company|Northpoint Business Center|C|Powermount employees receive the advertised discount.
What is mentioned about the workshops?|They will award certificates of achievement.|They will be held at the same site.|They will last for several months.|They require attendees to have company sponsorship.|C|The workshop series runs from February through May; each individual workshop lasts only a few hours.
According to the e-mail, what will Ms. Dutt send to Mr. Powell?|A directory of registered employees|A workshop questionnaire|Confirmation of her registration status|A discounted payment|D|She will transfer the discounted $60 fee after seat confirmation.
In the notice, the word “reasonably” in paragraph 1, line 2 is closest in meaning to|supremely|affordably|seasonally|wholly|B|Reasonably priced means affordably priced.
For which workshop is Ms. Dutt registering?|Creative Marketing Ideas|Introduction to Web Site Design|Powerful Presentation Applications|Advanced Online Research|B|The March workshop is Introduction to Web Site Design, with a discounted fee of $60.''')
extra(p,'''Who offers the workshops?|Multimedia Plus|Powermount's library|Fantasy Real Estate|Pomo|A|Multimedia Plus is the provider.
Where are most workshops held?|Southport Convention Center|Northpoint Business Center|Jeffco Community Center|Prince Street|B|Northpoint is the default venue.
How is participation described?|Compulsory|Invitation-only|Voluntary|Restricted to managers|C|The notice explicitly says participation is voluntary.
How much is the Powermount discount per workshop?|$5|$15|$20|$10|D|Employees receive a $10 discount.
On what date is Creative Marketing Ideas held?|February 23|March 29|April 16|May 8|A|Workshop 1 is on February 23.
What is the full fee for Introduction to Web Site Design?|$40|$70|$45|$50|B|Workshop 2 costs $70 before discount.
Which workshop uses the Southport venue?|Creative Marketing Ideas|Advanced Online Research|Introduction to Web Site Design|Powerful Presentation Applications|C|Only Workshop 2 has the alternate location.
When does Powerful Presentation Applications start?|9 A.M.|9:30 A.M.|10:30 A.M.|10 A.M.|D|Workshop 3 begins at 10 A.M.
What is the discounted fee for Advanced Online Research?|$40|$50|$60|$35|A|Workshop 4 costs $40 with the discount.
What does Ms. Dutt attach?|A receipt|A completed registration form|A portfolio|A menu|B|She encloses her completed form.
How will Ms. Dutt pay?|Cash at the door|Credit card by phone|Online bank transfer|Postal check|C|She states she will make an online bank transfer.
What must happen before Ms. Dutt pays?|The course must finish|Her manager must resign|The venue must move|A seat must be confirmed|D|Payment follows confirmation of an available seat.''')

p=passage('Pomo · Frequently asked questions and complaint', '''Pomo — Frequently Asked Questions (FAQ)

What exactly is Pomo?
Pomo is a marketplace where people all over the world can connect to sell and buy unique goods. Shoppers buy things they can't find anywhere else. It's that simple.

How do I become a seller?
If you want to sell your craft items on Pomo, first, please make sure they fit within our seller guidelines. You can visit pomo.com/guidelines to check. Then, visit pomo.com/sell to set up your shop. There will be a small security deposit fee of $15, but don't worry! You'll receive your security deposit fee back when your shop is confirmed by us.

When will I receive my purchase?
As a matter of fact, Pomo does not participate in the actual process of shipping or delivery. We provide a space, whether it's online or offline, and that's all we do. You can file a complaint if you receive a package unreasonably late or if you don't receive one at all. We will immediately issue a return or compensation and suspend the seller.

How does Pomo make money?
Our business model is based on shared success. There is a $0.25 listing fee for every item listed, and we receive 5% of all sales completed on our Web site. Of course, we also have revenue coming in from advertisements.

From: amyzhao@email.com
To: complaints@pomo.com
Date: May 14
Subject: Suspicious seller

Dear Pomo,
I have been a fan of your services for the past three years. I have been fortunate enough not to encounter any sellers that scammed me. However, I believe that I have been scammed. The shop is Skyblue Earrings. I saw that it sells glow-in-the-dark jewelry, so I purchased a set of its earrings. It's been three months since I ordered them, and now it is way past the estimated delivery date, which was March 21. I thought the delivery might have been delayed because the store is busy, but when I uploaded a review/comment about the delay, I was blocked from the shop. Please suspend them and give me a refund. My order number is 000000E289289.
Sincerely,
Amy Zhao''',3)
original(p,181,'''What is mentioned about Pomo?|It has many international locations.|It delivers products to customers.|It is not involved in any transactions.|It sells its own products.|C|Pomo provides the marketplace space and says it does not take part in the shipping or delivery process. Here the intended answer treats it as an intermediary; the wording “any transactions” is broader than the passage.|Câu gốc diễn đạt rộng; Pomo vẫn thu phí và 5% doanh số. Đáp án C theo ghi chú ảnh, cần hiểu trong ngữ cảnh vai trò trung gian.
What does the Web page indicate about the shops using Pomo?|They can sell whatever they want as long as the items are made by the sellers.|There are certain rules they must follow to be accepted as a shop.|There is a nonrefundable setup fee of $15 to establish a shop.|Pomo earns 15% of what the shops make.|B|Sellers must check and meet the seller guidelines.
What is the e-mail about?|A proposal for a new function|A request for promotion codes|A report of a questionable vendor|Directions to the headquarters|C|Amy reports a seller she believes has scammed her.
According to the Web page, how might Skyblue Earrings be affected?|Its service will be stopped by Pomo.|Its management will be replaced.|It will offer discounts on several items.|It will temporarily shut down its Web site.|A|Pomo says it will suspend the seller after such a complaint.
What made Ms. Zhao decide she was cheated?|Her purchase was not processed on her credit card.|Her colleagues had the same problems.|Her complaint was not accepted.|Her product was faulty.|C|She was blocked after posting a comment about the delay.''')
extra(p,'''What kind of goods is Pomo described as connecting people to buy and sell?|Unique goods|Only groceries|Only books|Only used cars|A|The FAQ describes a marketplace for unique goods.
What should a prospective seller check first?|The board agenda|The seller guidelines|The concert set list|The library hours|B|The first step is checking pomo.com/guidelines.
Where does a seller set up a shop?|pomo.com/help|pomo.com/refund|pomo.com/sell|pomo.com/music|C|The FAQ specifies pomo.com/sell.
How much is the security deposit?|$5|$10|$25|$15|D|The deposit is $15.
When is the security deposit returned?|When the shop is confirmed|After three years|When a customer complains|It is never returned|A|Pomo returns it after shop confirmation.
Who does not handle shipping or delivery?|Skyblue Earrings|Pomo|The individual seller|A courier|B|Pomo says it does not participate in that process.
What is the listing fee per item?|$15|$5|$0.25|$1.68|C|Each listed item costs $0.25.
What percentage of completed Web sales does Pomo receive?|15%|10%|25%|5%|D|Pomo receives 5% of completed sales.
What additional source of income is mentioned?|Advertisements|Library fines|Concert tickets|Property showings|A|The FAQ mentions advertising revenue.
How long has Amy used Pomo's services?|One year|Three years|Five months|Ten years|B|She has been a fan for the past three years.
What did Amy buy from Skyblue Earrings?|A bracelet|A necklace|A set of earrings|A watch|C|She purchased a set of glow-in-the-dark earrings.
What was the estimated delivery date?|May 14|May 21|February 20|March 21|D|The complaint specifies March 21.''')

p=passage('Pepperno Pizzeria · Expansion, job offer and table', '''Pepperno Pizzeria is proud to announce that we will be introducing at least four new branches in Asia. Located in China, South Korea, Japan and Taiwan, these four locations will be the spearhead of our project. Since we are venturing into new markets, we are in need of people that are willing to join our company. We will be acquiring the restaurant staff locally, but we have an entire new department that will deal with Asian affairs.

For entry-level positions, we are mainly looking for applicants that have a degree in finance, economy, international relations, or anything related to those. Although experience in the field is preferred, it is not necessary. However, for positions that involve being in charge, we require at least 5 years of experience. For more information about the application process or the complete job listing, visit our Web site at www.peppernopizzeria.com.

To: Allen Timm <atimm2291@email.com>
From: Lauren Malvo <LMalvo.1@pepperno.com>
Subject: Congratulations!
Date: May 12

Dear Mr. Timm,
Congratulations! We are pleased to offer you a full-time position as the head of advertisements at our Asian branches! As you already know, you will be in charge of the advertisements regarding our four branches in Asia. We were especially impressed with your experience as communications manager at Laiba Foods.
You will be starting work on May 21. Please report to the Human Resources office once you arrive since we will need you to fill out some documents. Please do not hesitate to call us if you have any questions prior to May 21. I can be reached at this e-mail address or by phone at 389-1289. Once again, welcome to Pepperno Pizzeria.
Sincerely,
Lauren Malvo
Human Resources Administrator, Pepperno Pizzeria

Jager F&B Magazine
Asia's Rising Top 5 Food & Beverage Companies, 2017
Rank / Company / Established / 2016 Revenue (US$ Billion) / Country
1 / Junun Group Ltd. / 2012 / $9.7 / China
2 / Tragos / 2007 / $8.2 / China
3 / Laiba Foods / 2011 / $7.6 / Japan
4 / GB F&B / 2009 / $6.1 / South Korea
5 / Ryson / 2014 / $4.9 / Taiwan''',3)
original(p,186,'''What is mentioned about Pepperno Pizzeria?|It is one of the top restaurants in Canada.|It has been around for more than a century.|It is notorious for treating its staff horribly.|It is expanding its business to Asia.|D|The advertisement announces at least four new Asian branches.
What positions do NOT require experience?|Entry-level positions|Management positions|Restaurant staff positions|Advertisement crew|A|Experience is preferred but not necessary for entry-level positions.
Why did Ms. Malvo send the e-mail to Mr. Timm?|To suggest a different option|To provide instructions|To assess his potential|To reject his job application|B|The offer provides his role, start date, and reporting instructions.
What is suggested about Mr. Timm?|He has already met Ms. Malvo.|He suggested the expansion to Asia.|He handed in his portfolio online.|He has at least 5 years of experience.|D|His leadership position requires at least five years of experience.
Where is the headquarters of Mr. Timm's previous company located?|China|Japan|South Korea|Taiwan|B|The table lists Laiba Foods under Japan.''')
extra(p,'''How many new Asian branches are announced at minimum?|Four|Two|Three|Ten|A|Pepperno announces at least four.
Which country is NOT among the four planned locations?|China|Thailand|Japan|Taiwan|B|The four are China, South Korea, Japan, and Taiwan.
How will restaurant staff be recruited?|Only from Canada|Only from head office|Locally|Through the library|C|The advertisement says staff will be acquired locally.
Which degree field is named for entry-level applicants?|Medicine|Architecture|Music|Finance|D|Finance is listed with economy and international relations.
How much experience is required for positions in charge?|At least five years|One month|Two years|None|A|Leadership positions require at least 5 years.
What job is Mr. Timm offered?|Communications manager at Laiba|Head of advertisements at the Asian branches|Restaurant chef|Magazine editor|B|This is the full-time position offered.
Where did Mr. Timm previously work?|Ryson|Tragos|Laiba Foods|GB F&B|C|The e-mail names Laiba Foods.
When will Mr. Timm start work?|May 12|May 1|March 21|May 21|D|His start date is May 21.
Where should he report upon arrival?|The Human Resources office|The kitchen|The rooftop|The Registration Department|A|He must report to HR to complete documents.
Which company ranks first in the table?|Laiba Foods|Junun Group Ltd.|Tragos|Ryson|B|Junun Group Ltd. is ranked 1.
What is Laiba Foods' listed 2016 revenue?|$9.7 billion|$8.2 billion|$7.6 billion|$4.9 billion|C|The Laiba row gives $7.6 billion.
Which company in the table is based in Taiwan?|GB F&B|Laiba Foods|Tragos|Ryson|D|Ryson is listed under Taiwan.''')

p=passage('Monday board meeting · Agenda, proposal and e-mail', '''Monday Board Meeting's Agenda
The weekly Monday board meeting will be addressing the following topics and adhering to the following agenda.
5:30–5:50 — Introductions and related news
5:50–6:40 — Recent market trends and competition moves
6:40–7:30 — Dinner
7:30–8:30 — Annual bonuses and raise freezes for employees
8:30–9:00 — Changing employee benefits
9:00–9:15 — Conclusion

As always, dinner will be served at the meeting and will arrive shortly after 6:30. Enclosed is the menu for this week and an order form. Please select your choices and have your administrative assistant call or fax in the order no later than noon on Monday. If you are unable to attend the board meeting, please e-mail Board Coordinator Amy Manning@GBC.com with any requests for meeting notes or an audio recording of the meeting for your review.

Proposal to Restructure Employee Benefits
By Tina Poland, Manager of Human Resources
As you know, this has been a tough year for our company, but instead of laying off employees, we have decided to restructure some benefits to ease our budget and to bring down costs. To that end, here are three different proposals to restructure employee benefits:
• Increase co-pays/deductibles for employer-sponsored health plans.
• Change the employer contribution to retirement plans to 25% ONLY if the employee sets up a maximum contribution plan instead of the current matching program.
• Offer employees time off without pay instead of changing benefits.
I believe option three is the best one, but, naturally, I will support the board's decision.

From: Robin Atkins
To: Amy Manning
Subject: Dinnertime
Date: April 13
Dear Ms. Manning,
I was just contacted by the catering company that is providing meals to our board meeting next Monday. The person said the dinner may be delayed by an hour due to a scheduling conflict. The meeting is imminent, so it is not easy to change catering companies. I heard that you are coordinating the meeting, so please take the appropriate actions.
Sincerely,
Robin Atkins''',2)
original(p,191,'''What can be inferred from the proposal?|The company is having a profitable year.|The company is anticipating many layoffs.|The company is trying to cut its budget.|The company lost its health insurance provider.|C|The proposal explicitly aims to ease the budget and reduce costs.
Why should a board member contact Amy Manning?|To reserve a seat at the meeting|To say that he or she is not attending|To give information on a meal preference|To make a suggestion for a topic for the meeting|B|Members unable to attend are directed to e-mail Amy for notes or a recording.
What time will Ms. Poland's proposal be given?|6:00|7:15|8:30|6:30|C|Her proposal concerns changing employee benefits, scheduled at 8:30.
In the e-mail, the word “imminent” in line 4 is closest in meaning to|advance|temporary|intense|near|D|Imminent means about to happen, or near.
What will most likely be affected by the dinner schedule change?|Introductions and related news|Recent market trends and competitor moves|Annual bonuses and raise freezes for employees|Changing employee benefits|B|A one-hour delay shifts dinner to around the 7:30–8:30 bonuses session, so the preceding market-trends discussion could be extended into the original dinner slot.|Đáp án B theo ghi chú sửa trên ảnh; câu hỏi suy luận về việc điều chỉnh lịch, không phải lịch mới đã được xác nhận.''')
extra(p,'''How often is the board meeting held?|Weekly on Monday|Monthly on Friday|Daily|Once a year|A|The agenda identifies a weekly Monday meeting.
What is the first agenda item?|Dinner|Introductions and related news|Employee benefits|Annual bonuses|B|Introductions are scheduled at 5:30.
When do market trends discussions start?|5:30|6:40|5:50|8:30|C|The market-trends slot begins at 5:50.
What is the original dinner slot?|5:30–5:50|7:30–8:30|8:30–9:00|6:40–7:30|D|The agenda gives 6:40–7:30 for dinner.
What topic occupies 7:30–8:30?|Annual bonuses and raise freezes|Introductions|Conclusion|Employee benefits|A|The agenda assigns this hour to bonuses and raise freezes.
When does the meeting conclude according to the agenda?|9:00|9:15|8:30|7:30|B|The conclusion ends at 9:15.
By what time must meal orders be submitted?|Friday evening|Monday 5 P.M.|Noon on Monday|Tuesday morning|C|Orders must be called or faxed by noon Monday.
Who should call or fax the meal order?|The cashier|The conductor|The librarian|The member's administrative assistant|D|The instructions assign this to the administrative assistant.
Who wrote the employee-benefits proposal?|Tina Poland|Robin Atkins|Amy Manning|Lauren Malvo|A|The proposal is by Tina Poland.
What is Tina Poland's position?|Board Coordinator|Manager of Human Resources|Catering Director|Journal Editor|B|Her title is Manager of Human Resources.
Which proposal does Ms. Poland prefer?|Increasing co-pays|Changing retirement contributions|Offering unpaid time off|Laying off employees|C|She believes option three is best.
Why might dinner be delayed?|Bad weather|Lack of a kitchen|A menu change|A scheduling conflict|D|The caterer reports a scheduling conflict.''')

p=passage('Business Builders Club · Journal and e-mails', '''Journal of Modern Social Psychology
April — Volume 204
Table of Contents
LETTER FROM EDITOR — 1
Working Together: Bridging the Gap between Different Cultures — 2
Authors: Raymond McPherson, Emily Jensen, Meredith Kwan
Body Language and What It Can Tell You — 19
Authors: Mary Colvin, Charles Bryant, Carol Ward
Social Networking Sites and Their Consequences — 35
Authors: Inez Davis, Oscar Otero
Finding the Inspiration and Motivation within You — 51
Authors: Ernest Sims, Shawna Lebrie, Miles Lund, Henry Phyon
Note: Lead researchers are listed first, with assistant researchers following, alphabetically.

To: Charles Bryant <c.bryant@augustauni.edu>
From: Maria Lawton <lawtonm@wss.net>
Date: May 27
Subject: From the Business Builders Club

Dear Mr. Bryant,
I am writing to you on behalf of the Business Builders Club. We are an organization of professionals that meet once every quarter to learn new skills that are applicable to our careers. I saw your lecture at the Roseville Public Library on May 12, and I was really impressed with how much I learned in such a short time. You are obviously a talented and knowledgeable presenter. I think our members will appreciate the insights you can share into how to improve communications skills. Therefore, I'm wondering if you would be available to attend one of our sessions and give a presentation on your research. We are particularly interested in the paper that was published in the April issue of the Journal of Modern Social Psychology. Please let me know your availability and fees. Our next two meetings are September 20 and December 28. You can reach me at this e-mail address or by phone at 555-4059.
Warmest regards,
Maria Lawton
President, Business Builders Club

To: Maria Lawton <lawtonm@wss.net>
From: Charles Bryant <c.bryant@augustauni.edu>
Date: May 28
Subject: RE: From the Business Builders Club

Dear Ms. Lawton,
Thank you for your kind words. I'm pleased you were able to attend the talk in Roseville. In fact, that was my very first stop on the tour. The library director there did an excellent job promoting the event to ensure a high turnout. As for your request, unfortunately, I have plans to teach overseas this coming semester. However, I've spoken to Mary Colvin, and she is interested in visiting your group. I've passed along your phone number, and you can expect a call from her sometime next week. I've also asked my colleague to e-mail you the handouts from the Roseville lecture since we ran out of them that day.
Sincerely,
Charles Bryant''',1)
original(p,196,'''What is NOT a topic covered in the journal?|Learning a foreign language|Cross-cultural interactions|The effects of social media|Self-motivation|A|The contents cover culture, body language, social networking, and motivation, but not foreign-language learning.
What is the purpose of the first e-mail?|To offer research assistance|To thank Mr. Bryant for his help|To recruit a new member for a club|To invite Mr. Bryant to give a talk|D|Maria asks him to attend a session and present his research.
What is indicated about the Business Builders Club?|It meets at the Roseville Public Library.|It is a newly formed organization.|It has meetings four times a year.|It is exclusively for business owners.|C|Once every quarter means four meetings a year.
What is true about Mr. Bryant's lecture tour?|It will happen again next year.|It had some lectures overseas.|It mainly visited universities.|It started on May 12.|D|The May 12 Roseville talk was the first stop on his tour.
Who will call Ms. Lawton next week?|A journal editor|A lead researcher|Mr. Bryant's assistant|A library director|B|Mary Colvin is listed first for the body-language paper, making her the lead researcher.''')
extra(p,'''Which journal issue is shown?|April, Volume 204|May, Volume 201|June, Volume 54|March, Volume 147|A|The contents heading gives April, Volume 204.
On which page does the cross-cultural paper begin?|1|2|19|35|B|Working Together starts on page 2.
Which paper begins on page 19?|Social Networking Sites|Working Together|Body Language and What It Can Tell You|Finding the Inspiration|C|Body Language starts on page 19.
Who is the lead researcher of the body-language paper?|Charles Bryant|Carol Ward|Inez Davis|Mary Colvin|D|Mary is listed first; the note identifies the first name as lead researcher.
Which topic starts on page 35?|Social networking sites|Body language|Employee benefits|Foreign languages|A|Social Networking Sites and Their Consequences begins on page 35.
Who is the lead researcher of the self-motivation paper?|Shawna Lebrie|Ernest Sims|Henry Phyon|Miles Lund|B|Ernest Sims is listed first.
What is Maria Lawton's role?|Journal editor|University dean|President of the Business Builders Club|Library director|C|Her signature identifies her as club president.
Where did Maria hear Mr. Bryant speak?|Jeffco Community Center|Northpoint Business Center|An Asian branch|Roseville Public Library|D|She attended his lecture at Roseville Public Library.
What are the club's next two meeting dates?|September 20 and December 28|May 27 and May 28|April 13 and May 1|March 21 and May 14|A|The first e-mail gives these two dates.
Why can Mr. Bryant not accept the invitation?|He is retiring|He plans to teach overseas|He has no research|He cannot contact Maria|B|He will teach overseas during the coming semester.
Who helped promote the Roseville event?|The club treasurer|A magazine cashier|The library director|A caterer|C|Mr. Bryant credits the library director.
Why will a colleague e-mail lecture handouts?|The lecture was canceled|The club lost its copies|The handouts were never printed|They ran out at the lecture|D|Mr. Bryant says they ran out that day.''')

questions.sort(key=lambda q:(q['kind']=='extra',int(q['number']) if q['kind']=='original' else int(q['number'][2:])))
data={'passages':passages,'questions':questions}
(ROOT/'data.js').write_text('window.QUIZ_DATA = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
assert [int(q['number']) for q in questions if q['kind']=='original']==list(range(147,201))
assert len(questions)>200
assert all(len(q['options'])==4 and 0<=q['answer']<4 for q in questions)
print(f'{len(passages)} reading groups; {len(questions)} questions: 54 originals + {len(questions)-54} supplementary.')
