<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tennis: Earnings vs Popularity | Anna Jurek</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', 'Times New Roman', Times, serif;
            line-height: 1.6;
            color: #1a1a1a;
            background: #fafafa;
            padding: 40px 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 40px 50px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        h1 {
            font-size: 2.2rem;
            margin-bottom: 0.5rem;
            color: #0a0a0a;
            border-left: 4px solid #e91e63;
            padding-left: 20px;
        }

        .author {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 2rem;
            border-bottom: 1px solid #eee;
            padding-bottom: 1rem;
        }

        h2 {
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: #222;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 0.3rem;
        }

        h3 {
            font-size: 1.2rem;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
            color: #333;
        }

        p {
            margin-bottom: 1rem;
        }

        iframe {
            margin: 1.5rem 0;
            border: 1px solid #ddd;
            border-radius: 8px;
            background: #f9f9f9;
            width: 100%;
        }

        .caption {
            font-size: 0.8rem;
            color: #666;
            text-align: center;
            margin-top: -1rem;
            margin-bottom: 1.5rem;
            font-style: italic;
        }

        hr {
            margin: 2rem 0;
            border: none;
            border-top: 1px solid #eee;
        }

        .data-source {
            font-size: 0.8rem;
            color: #666;
            background: #f5f5f5;
            padding: 1rem;
            border-radius: 6px;
            margin-top: 2rem;
        }

        @media (max-width: 700px) {
            .container {
                padding: 20px;
            }
            h1 {
                font-size: 1.6rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Do tennis players' high earnings go hand in hand with their popularity?</h1>
        <div class="author">Author: Anna Jurek | Date: May 6, 2026</div>

        <p>It is widely known that tennis players are among the highest-paid athletes, and the most popular matches attract millions of people. However, are earnings and popularity synonymous, and what does it mean in today's world to search for someone on a search engine versus having them followed on Instagram? This analysis looks at the 20 female players at the top of the WTA rankings as of May 4, 2026.</p>

        <h2>Chart 1: Earnings vs. Instagram Followers</h2>
        <iframe src="https://raw.githubusercontent.com/data-journalism-26/data-bit-2-anna_db2/main/output/scatter.html" width="100%" height="600px" style="border:none;"></iframe>
        <div class="caption">Data from Wikipedia, Instagram, and wtatennis.com. Bubble size = Wikipedia page views. Color = WTA ranking (green = higher rank).</div>

        <p>It is clearly evident that earnings are positively correlated with Instagram popularity. If we were to draw a trend line, it would slope upward. However, there are a few outliers.</p>

        <p>Naomi Osaka is the second most followed player on Instagram among the group but only sixth in terms of career prize money earned on the court. Coco Gauff ranks at the same level of popularity as Iga Świątek despite earning significantly less money so far in her career.</p>

        <p>It is also worth noting that among less popular players, there is not necessarily a trend of higher earnings following higher popularity. Madison Keys and Jessica Pegula both have fewer than 500,000 Instagram followers, yet their combined career tournament earnings exceed $20 million.</p>

        <h2>Chart 2: Wikipedia vs. Instagram</h2>
        <iframe src="https://raw.githubusercontent.com/data-journalism-26/data-bit-2-anna_db2/main/output/wiki_vs_instagram.html" width="100%" height="600px" style="border:none;"></iframe>
        <div class="caption">Data from Wikipedia, Instagram, and wtatennis.com. Bubble size = career earnings. Sabalenka removed as outlier.</div>

        <p>To understand how these players perform on Wikipedia searches, we can look at the second chart. Jessica Pegula, Madison Keys, and Elena Rybakina – who are not very popular on Instagram – rank very high in terms of monthly searches on Wikipedia.</p>

        <p>This phenomenon can be partly explained by a different target audience. Jessica Pegula and Madison Keys are older players who have been on the tour for many years. Their careers may not appeal to typical Instagram users who follow younger, more media-friendly athletes. In contrast, Coco Gauff is young and often portrayed in the media as the next Serena Williams, which drives both Instagram followers and Wikipedia curiosity.</p>

        <h2>Conclusion</h2>
        <p>It is clear that top-ranked players are very popular, but not all of them necessarily draw crowds with their personalities. On the court, personality does not matter, and the biggest prize money ultimately goes to the player who wins matches.</p>

        <p>Another aspect worth examining is earnings from advertising contracts, which are certainly positively correlated with popularity. But few people need a study to confirm that relationship. The more surprising finding is that some players – like Rybakina, Pegula, and Keys – earn millions without building large Instagram followings. They appeal to a different, perhaps older, audience that searches for them on Wikipedia but does not follow them on social media.</p>

        <p>Tennis has two attention economies. One rewards the young and the charismatic. The other rewards the consistent and the respected. The smartest players find a way to win in both.</p>

        <div class="data-source">
            <strong>Data sources:</strong> WTA official rankings and career earnings (wtatennis.com, May 2026), Instagram follower counts (manual collection), Wikipedia page view statistics (Wikimedia API, April 2026). Aryna Sabalenka excluded from second chart only as a statistical outlier.
        </div>
    </div>
</body>
</html>