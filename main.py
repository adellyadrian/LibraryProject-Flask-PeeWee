from data import Books


Books.create(
    title='Hamlet',
    year=1599,
    author='William Shakespeare',
    content="The Tragedy of Hamlet, Prince of Denmark, often shortened to Hamlet (/ˈhæmlɪt/), "
            "is a tragedy written by William Shakespeare sometime between 1599 and 1601. It is Shakespeares longest play,"
            " with 29,551 words. Set in Denmark, the play depicts Prince Hamlet and his attempts to exact revenge"
            " against his uncle, Claudius, who has murdered Hamlets father in order to seize his throne and marry Hamlets mother."
            "Hamlet is considered among the most powerful and influential tragedies in the English language, with a story capable of "
            "seemingly endless retelling and adaptation by others."
            "There are many works that have been pointed to as possible sources for Shakespeare's play—from ancient "
            "Greek tragedies to Elizabethan plays. The editors of the Arden Shakespeare question the idea of source hunting,"
            "pointing out that it presupposes that authors always require ideas from other works for their own, "
            "and suggests that no author can have an original idea or be an originator. When Shakespeare wrote, "
            "there were many stories about sons avenging the murder of their fathers, and many about clever avenging "
            "sons pretending to be foolish in order to outsmart their foes. This would include the story of the ancient Roman, "
            "Lucius Junius Brutus, which Shakespeare apparently knew, as well as the story of Amleth, which was preserved "
            "in Latin by 13th-century chronicler Saxo Grammaticus in his Gesta Danorum, and printed in Paris in 1514. "
            "The Amleth story was subsequently adapted and then published in French in 1570 by the 16th-century scholar "
            "François de Belleforest. It has a number of plot elements and major characters in common with Shakespeares Hamlet,"
            " and lacks others that are found in Shakespeare. Belleforests story was first published in English in 1608, "
            "after Hamlet had been written, though its possible that Shakespeare had encountered it in the French-language version."
            "Three different early versions of the play are extant: the First Quarto (Q1, 1603); the Second Quarto (Q2, 1604);" 
            "and the First Folio (F1, 1623). Each version includes lines and passages missing from the others.",
    isbn='9780140707342',
    image='https://pup-assets.imgix.net/onix/images/9780691166841.jpg',
    status=3
)

Books.create(
    title='The Great Gatsby',
    year=1925,
    author='F. Scott Fitzgerald',
    content="The Great Gatsby is a 1925 novel by American writer F. Scott Fitzgerald."
            " Set in the Jazz Age on Long Island, near New York City, the novel depicts first-person narrator "
            "Nick Carraway's interactions with mysterious millionaire Jay Gatsby and Gatsby's obsession to reunite "
            "with his former lover, Daisy Buchanan.",
    isbn='9780333791035',
    image='https://images2.penguinrandomhouse.com/cover/9780593201077',
    status=3
)

Books.create(
    title='War and Peace',
    year=1869,
    author='Leo Tolstoy',
    content="War and Peace[a] is a literary work by Russian author Leo Tolstoy. Set during the Napoleonic Wars, "
            "the work mixes fictional narrative with chapters on history and philosophy. "
            "First published serially beginning in 1865, the work was rewritten and published in its entirety in 1869."
            " It is regarded as Tolstoy's finest literary achievement and remains an internationally praised classic"
            " of world literature.",
    isbn='9788412664812',
    image='https://cdn.penguin.co.uk/dam-assets/books/9781448142675/9781448142675-jacket-large.jpg',
    status=3
)
Books.create(
    title='Lolita',
    year=1955,
    author='Vladimir Nabokov',
    content="Lolita is a 1955 novel written by Russian-American novelist Vladimir Nabokov. "
            "The novel is notable for its controversial subject: the protagonist and unreliable narrator, "
            "a middle-aged literature professor under the pseudonym Humbert Humbert, is obsessed with a 12-year-old girl"
            ", Dolores Haze, whom he kidnaps and sexually abuses after becoming her stepfather. 'Lolita',"
            " the Spanish nickname for Dolores, is what he calls her privately. The novel was originally written"
            " in English and first published in Paris in 1955 by Olympia Press.",
    isbn='9783498046460',
    image='https://api.time.com/wp-content/uploads/2015/07/lolita.jpeg',
    status=3
)

Books.create(
    title="Alice's Adventures in Wonderland",
    year=1865,
    author='Lewis Carroll',
    content="Alice's Adventures in Wonderland (commonly Alice in Wonderland) is an 1865 English children's novel "
            "by Lewis Carroll, a mathematics don at Oxford University. It details the story of a young girl named Alice"
            " who falls through a rabbit hole into a fantasy world of anthropomorphic creatures. It is seen as an example "
            "of the literary nonsense genre. The artist John Tenniel provided 42 wood-engraved illustrations for the book.",
    isbn='9780194229647',
    image='https://m.media-amazon.com/images/I/91uMrXq+4RL._AC_UF894,1000_QL80_.jpg',
    status=3
)

Books.create(
    title='One Thousand and One Nights',
    year=1706,
    author='Alf Laylah wa-Laylah',
    content="One Thousand and One Nights (Arabic: أَلْفُ لَيْلَةٍ وَلَيْلَةٌ, romanized: ʾAlf Laylah wa-Laylah)[1] is a collection "
            "of Middle Eastern folk tales compiled in Arabic during the Islamic Golden Age. It is often known in English "
            "as the Arabian Nights, from the first English-language edition (c. 1706–1721), which rendered the title"
            " as The Arabian Nights' Entertainment.",
    isbn='9780706411157',
    image='https://www.bfbooks.com/core/media/media.nl?id=2146&c=426867&h=aTq93H1LNGPz6b-E_M3XoZ3cGZmxxM-NqMoMLMqWJKav3kMO',
    status=3
)

Books.create(
    title='Sapiens',
    year=2011,
    author=' Yuval Noah Harari',
    content="Sapiens: A Brief History of Humankind (Hebrew: קיצור תולדות האנושות, [Ḳitsur toldot ha-enoshut]) "
            "is a book by Yuval Noah Harari, first published in Hebrew in Israel in 2011 based on a series of "
            "lectures Harari taught at The Hebrew University of Jerusalem, and in English in 2014.[1][2] The book, "
            "focusing on Homo sapiens, surveys the history of humankind, starting from the Stone Age and going up to "
            "the twenty-first century. The account is situated within a framework that intersects the natural sciences"
            " with the social sciences.",
    isbn=' 9780062316097',
    image='https://dynamic.indigoimages.ca/v1/books/books/0771038518/1.jpg?width=614&maxheight=614&quality=85',
    status=3
)

Books.create(
    title='Women & Power: A Manifesto',
    year=2017,
    author='Mary Beard',
    content="At long last, Mary Beard addresses in one brave book the misogynists and trolls who mercilessly attack "
            "and demean women the world over, including, very often, Mary herself. In Women & Power, she traces the"
            " origins of this misogyny to its ancient roots, examining the pitfalls of gender and the ways that history"
            " has mistreated strong women since time immemorial. As far back as Homer’s Odyssey, Beard shows, women have"
            " been prohibited from leadership roles in civic life, public speech being defined as inherently male."
            " From Medusa to Philomela (whose tongue was cut out), from Hillary Clinton to Elizabeth Warren "
            "(who was told to sit down), Beard draws illuminating parallels between our cultural assumptions"
            " about women’s relationship to power—and how powerful women provide a necessary example for all women"
            " who must resist being vacuumed into a male template. ",
    isbn='9783103973990',
    image='https://m.media-amazon.com/images/I/610LMqdBAlL._AC_UF1000,1000_QL80_.jpg',
    status=3
)

Books.create(
    title='To Kill a Mockingbird',
    year=1960,
    author='Harper Lee',
    content="To Kill a Mockingbird is a novel by the American author Harper Lee. It was published in 1960 "
            "and was instantly successful. In the United States, it is widely read in high schools and middle schools."
            " To Kill a Mockingbird has become a classic of modern American literature; a year after its release, "
            "it won the Pulitzer Prize. The plot and characters are loosely based on Lee's observations of her family,"
            " her neighbors and an event that occurred near her hometown of Monroeville, Alabama, in 1936, when she was ten.",
    isbn='9780140707342',
    image='https://cdn.britannica.com/21/182021-050-666DB6B1/book-cover-To-Kill-a-Mockingbird-many-1961.jpg',
    status=3
)

Books.create(
    title='The Road Back',
    year=1931,
    author='Erich Maria Remarque',
    content="The Road Back, also translated as The Way Back,[1] (German: Der Weg zurück) is a novel by German author "
            "Erich Maria Remarque, commonly regarded as a sequel to his 1929 novel All Quiet on the Western Front."
            " It was first serialized in the German newspaper Vossische Zeitung between December 1930 and January 1931,"
            " and published in book form in April 1931.",
    isbn='9781299873728',
    image='https://m.media-amazon.com/images/M/MV5BYjliNGFlNjMtMzJiZS00ZmIzLTkyYjQtZWRhOWNiMWE2Y2I4XkEyXkFqcGdeQXVyNzQzNzQxNzI@._V1_.jpg',
    status=3
)

Books.create(
    title='The Sun and the Star',
    year=2023,
    author='Rick Riordan and Mark Oshiro',
    content="Two months after the defeat of Nero and Python, Rachel Elizabeth Dare provides the prophecy for Nico di Angelo and his boyfriend Will Solace's quest into Tartarus to rescue the Titan Iapetus, better known as Bob, for the twelfth time. Concerned that Bob's situation must be getting more dire, Nico convinces a reluctant Chiron and Mr. D to issue them an official quest. Before departing, the two contact Percy Jackson and Annabeth Chase for advice based upon their own experience in Tartarus. Making their way into the Underworld through the Door of Orpheus, which Nico and Percy had previously used, the two demigods are immediately set upon by the demon of nightmares, Epiales, who reveals that their mother is after Nico before Will manages to kill the demon using his newly-discovered power to emit light. Nico and Will seek out the help of the troglodytes, who agree to lead them to a shortcut to Tartarus. But first, they pass the farm of Menoetes, who only agrees not to tell Hades about their quest in exchange for some stolen fruit from Persephone's garden. Although the heist is successful, Will encounters Persephone herself, who offers him advice on his struggles to understand Nico, suggesting that Will embrace his own inner darkness rather than rejecting it, before gifting Will the stolen pomegranates.",
    isbn='9781368098878',
    image='https://m.media-amazon.com/images/I/81v4hS6N09L.jpg',
    status=3
)

Books.create(
    title='The Half Moon',
    year=2023,
    author='Meri Bet Kin',
    content="Malcolm Gephardt, handsome and gregarious longtime bartender at the Half Moon, has always dreamed of owning a bar. When his boss finally retires, Malcolm stretches to buy the place. He sees unquantifiable magic and potential in the Half Moon and hopes to transform it into a bigger success, but struggles to stay afloat. His smart and confident wife, Jess, has devoted herself to her law career. After years of trying for a baby, she is facing the idea that motherhood may not be in the cards for her. Like Malcolm, she feels her youth beginning to slip away and wonders how to reshape her future. Award-winning author Mary Beth Keane’s new novel takes place over the course of one week when Malcolm learns shocking news about Jess, a patron of the bar goes missing, and a blizzard hits the town of Gillam, trapping everyone in place. With a deft eye and generous spirit, Keane explores the disappointments and unexpected consolations of midlife, the many forms forgiveness can take, the complicated intimacy of small-town living, and what it means to be a family.",
    isbn=9781797154718,
    image='https://m.media-amazon.com/images/I/81LwAH4tCBL._AC_UF1000,1000_QL80_.jpg',
    status=3
)

Books.create(
    title='Ascension',
    year=2023,
    author='Nicholas Binge',
    content="An enormous snow-covered mountain has appeared in the Pacific Ocean. No one knows when exactly it showed up, precisely how big it might be, or how to explain its existence. When Harold Tunmore is contacted by a shadowy organization to help investigate, he has no idea what he is getting into as he and his team set out for the mountain. The higher Harold’s team ascends, the less things make sense. Time moves differently, turning minutes into hours, and hours into days. Amid the whipping cold of higher elevation, the climbers’ limbs numb and memories of their lives before the mountain begin to fade. Paranoia quickly turns to violence among the crew, and slithering, ancient creatures pursue them in the snow. Still, as the dangers increase, the mystery of the mountain compels them to its peak, where they are certain they will find their answers. Have they stumbled upon the greatest scientific discovery known to man or the seeds of their own demise? Framed by the discovery of Harold Tunmore’s unsent letters to his family and the chilling and provocative story they tell, Ascension considers the limitations of science and faith and examines both the beautiful and the unsettling sides of human nature.",
    isbn=9781601637543,
    image='https://m.media-amazon.com/images/I/91leSx3aH1L._AC_UF1000,1000_QL80_.jpg',
    status=3
)

Books.create(
    title='Zero to One',
    year=2014,
    author='Peter Thiel with Blake Masters',
    content="In The Atlantic, Derek Thomson describes Thiel's book as possibly the best business book he has ever read. In his review article, he wrote: 'Peter Thiel's new book, Zero to One, shines like a laser beam. Yes, this is a self-help book for entrepreneurs, bursting with bromides and sunny confidence about the future that only start-ups can build. But much more than that, it's also a lucid and profound articulation of capitalism and success in the 21st century economy' and 'it's surprising in a wonderful way just how simple Zero to One feels. Barely 200 pages long, and well lit by clear prose and pithy aphorisms, Thiel has written a perfectly tweetable treatise and a relentlessly thought-provoking handbook'. Publishers Weekly wrote of the book: 'Thiel touches on how to build a successful business, but the discussion is too abstract to offer much to the next Steve Jobs—or Peter Thiel.' In November 2014, Timothy B. Lee reviewed the book for Vox.com, writing that although Thiel's book contained some good advice, he made the advice sound more contrarian than it really was, did not provide sufficiently concrete advice, and made some questionable claims.",
    isbn=9780804139298,
    image='https://m.media-amazon.com/images/I/71RQ0N83RGL._AC_UF1000,1000_QL80_.jpg',
    status=3
)
