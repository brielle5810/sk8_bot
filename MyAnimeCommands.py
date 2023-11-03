#this cog uses the MyAnimeList and AniList APIs
import requests
import discord
from discord.ext import commands
import json
import random


class MyAnimeCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("MAC.py is ready!")

    #details on available genres:
    @commands.command()
    async def genres(self, ctx):
        embed_var=discord.Embed(title="Available genres for !animerec {genre}:\n\n",description="\n\nAction, Adventure, Comedy, Drama, Ecchi, Fantasy, Horror, Mahou Shoujo, Mecha, Music, Mystery,"
                                                     "Psychological, Romance, Sci-Fi, Slice of Life, Sports, Supernatural, and Thriller.\n\nEnter the genre without {curly braces}.\nExample: !animerec Action",color=discord.Color.blurple())
        await ctx.send(embed=embed_var)

    #MAL reccomendation from the recc page
    @commands.command()
    async def recme(self, ctx):
        url = "https://myanimelist.p.rapidapi.com/anime/recommendations/1"
        headers = {
            "X-RapidAPI-Key": "YOUR_KEY_HERE",
            "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"}
        response = requests.get(url, headers=headers)
        json_data = json.loads(response.text)
        number = random.randint(0, 98)

        title=json_data['recommendations'][number]['recommendation']['title']
        pic_url=json_data['recommendations'][number]['recommendation']['picture_url']
        desc=json_data['recommendations'][number]['description']

        embed_var = discord.Embed(title="My Anime List users recommends:", description=f"{title}\n \n{desc}",
                                  color=discord.Color.dark_teal())
        embed_var.set_thumbnail(url=pic_url)
        await ctx.send(embed=embed_var)

    @commands.command()
    async def animerec(self,ctx, user_genre):
        if user_genre=="Mahou":
            user_genre="Mahou Shoujo"
        if user_genre == "Slice":
            user_genre = "Slice of Life"
        print(user_genre)
        genre_list=["Action", "Adventure", "Comedy", "Drama", "Ecchi", "Fantasy",
                    "Horror", "Mahou Shoujo", "Mecha", "Music", "Mystery", "Psychological",
                    "Romance", "Sci-Fi", "Slice of Life", "Sports", "Supernatural", "Thriller"]
        if user_genre in genre_list:
            query = ''' 
            query($page: Int, $perPage: Int, $genre: String) {
                Page(page: $page, perPage: $perPage) {
                    pageInfo {
                    total
                    currentPage
                    lastPage
                    hasNextPage
                    perPage
                    }
                    media(genre: $genre) {
                        title {
                        romaji
                        english
                        }
                    }
                }
            }
            '''
            url = 'https://graphql.anilist.co'
            number = random.randint(0, 1000)

            try:
                url = 'https://graphql.anilist.co'
                number = random.randint(0, 1000)
                print(number)
                variables = {'genre': user_genre, 'page': number, 'perPage': 1}
                response = requests.post(url, json={'query': query, 'variables': variables})
                json_data = json.loads(response.text)
                if json_data['data']['Page']['media'][0]['title']['english'] is None or type(
                        json_data['data']['Page']['media'][0]['title']['english']) != str:
                    print(json_data['data']['Page']['media'][0]['title']['english'])
                    assert False

                elif (json_data['data']['Page']['media'][0]['title']['english']) == "None":
                    print("none pizza left beef")
                    rec = ("Reccomendation: \n\n"
                            "English: " + json_data['data']['Page']['media'][0]['title']['romaji'] + "\n\n"
                                                                                                     "Romaji: " +
                            json_data['data']['Page']['media'][0]['title']['romaji'])
                else:
                    print('here!')
                    print(json_data['data']['Page']['media'][0]['title']['english'])
                    rec = ("Reccomendation: \n\n"
                            "English: " + json_data['data']['Page']['media'][0]['title']['english'] + "\n\n"
                                                                                                      "Romaji: " +
                            json_data['data']['Page']['media'][0]['title']['romaji'])
            except:
                number = random.randint(0, 25)
                print(number)
                variables = {'genre': user_genre, 'page': number, 'perPage': 1}
                print("last, resort,,,,")
                response = requests.post(url, json={'query': query, 'variables': variables})
                json_data = json.loads(response.text)
                print(json_data)
                number = 0

                while (type(json_data['data']['Page']['media'][0]['title']['english']) != str or
                       json_data['data']['Page']['media'][0]['title']['english'] == "None" or
                       json_data['data']['Page']['media'][0]['title']['english'] is None):
                    number += 1
                    response = requests.post(url, json={'query': query, 'variables': variables})
                    json_data = json.loads(response.text)
                    if number > 4:
                        break

                if number > 4:
                    variables = {'genre': user_genre, 'page': 5, 'perPage': 1}
                    response = requests.post(url, json={'query': query, 'variables': variables})
                    json_data = json.loads(response.text)
                rec= ("Reccomendation: \n\n"
                        "English: " + json_data['data']['Page']['media'][0]['title']['english'] + "\n\n"
                                                                                                  "Romaji: " +
                        json_data['data']['Page']['media'][0]['title']['romaji'])

            embed_var = discord.Embed(title=f"Genre: {user_genre}", description=f"\n{rec}",
                                      color=discord.Color.random())
            await ctx.send(embed=embed_var)
        else:
            embed_var=discord.Embed(title="Sorry! There was an error!",description="\nError is likely either too many requests or faulty requests.\n\n Please wait a moment before trying again. \n"
                                                                                   "\nDouble check your requested genre as well. Available genres include:\n"
                                                                                   "\nAction, Adventure, Comedy, Drama, Ecchi, Fantasy, Horror, Mahou Shoujo, Mecha, Music, Mystery, "
                                                     "Psychological, Romance, Sci-Fi, Slice of Life, Sports, Supernatural, and Thriller.",color=discord.Color.dark_orange())
            await ctx.send(embed=embed_var)


async def setup(client):
    await client.add_cog(MyAnimeCommands(client))
