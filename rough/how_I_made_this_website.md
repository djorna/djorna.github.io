Title: How to build a blog for free with Pelican
Date: 2019-07-01 20:40
Modified: 2019-07-01 20:40
Category: Tutorials
Tags: Programming, Python
Slug: how-to-build-a-blog-for-free-with-pelican
Authors: David Jorna
Summary: How to build a static website for free with no hosting fees, with minimal coding experience.
Featured_Image: /images/pelican_logo.png


Two blog posts in and I'm already scraping the bottom of the barrel. Rest assured, I haven't run out of ideas, but some of my other post ideas will take a bit longer to write, so this will have to do for now.

# Why use a static site generator?
Most "How to Start a Blog" advice will advise you to use a CMS like WordPress, pick a host

# Do I have to know how to code?
Some fundamental programming skills will by helpful if you want to edit your theme, which you almost definitely will.




# This sounds too good to be true. If you can make a blog for free, why do people pay for WordPress hosting?
![pick-two](images/pick_two.png)

>Good, fast cheap. Pick two.

It's the new widely-known and frequently repeated mantra of web development. I would tell you where the quote comes from, but to my irritation, I wasn't able to find the source online. It seems to be derived from the [project management triangle](https://en.wikipedia.org/wiki/Project_management_triangle), but even the omniscient nerds at Wikipedia don't seem to know where this concept originated.

In any case, using a static site generator is a sort of DIY approach, so it falls into the "good and cheap, but not fast" category. So the trade-off you're making by using a static site generator is that it might take you a bit longer to get set up. 


# Choosing a static site generator
There are several different SSGs out there, and you could waste a lot of valuable time weighing the pros and cons of each one. So let's do that.

Before looking at the pros and cons, I recommend considering the following factors when making your selection:
* Pick one written in a language you know already, or a language you want to learn. I decided against using Jekyll for this reason, since I don't intend to ever use Ruby for anything.
* Speed doesn't really matter. The speed of an SSG is just how fast the pages are generated. This may be a bit more convenient while editing your theme, but otherwise this is of little importance.
* How good is the selection of templates? This is especially important if you're not a web designer, or don't want to spend a lot of time tweaking your theme. 
* 

Here's a list of some popular SSGs. It's not an exhaustive list, nor is it in any particular order.

## 1. Hugo (written in golang)
Pros:
* Fast generation
* Nice selection of templates
* Widely used, so 

## 2. Jekyll (written in Ruby)
Pros:
* Most widely used option
* Endorsed by Github Pages (note that any SSG will work with Github Pages; this just means you'll have to use your brain less)

## 3. Pelican (written in Python)
Pros:
* Most Pythonic

Cons:
* Not as popular as the other options
* Theme selection is much lower than 


# Getting started with Pelican
I chose to use a static site generator called Pelican for my blog, since I already had some experience with Python. Pelican's website has a great tutorial for getting started,but there's a few things you'll want to do to integrate with Github Pages, and improve your workflow.

## 1. Workflow
Your blog posts will be written in Markdown, so I recommend using a text editor such as [VSCode](https://code.visualstudio.com/), which will allow you to preview the appearance of your posts in real time, and give you access to spell-checking plugins

To preview your website locally, you will have to first generate content with
```Python
pelican content
```
Then listen on your local network with
```Python
pelican --listen
```
If you don't like typing `pelican content` every time you want to see changes, you can set pelican to run it automatically every time you make a change, which I recommend.
```Python
pelican content --autoreload
```
Since I normally use a Windows desktop, I made a little batch script to do all of this automatically.
```Bat
# start.bat
CALL ../env/Scripts/activate.bat # Activate Python virtual environment
START "new window" cmd /k "pelican --listen" # Create a new terminal, and listen on localhost:8000 (or whatever address you set)
pelican content --autoreload # Automatically re-generate your content when you make changes
```
For Linux users, here's the equivalent bash script:
```Bash
../env/bin/activate

```

To deploy your blog through Github Pages, [this blog post](https://rasor.github.io/using-pelican-blog-on-github-pages.html) includes a batch script to commit and push your changes to master, then checkout your development branch again. I'll include it here for convenience:
```Bat
# publish.bat
git add .
git commit -a -m %1
git push -u origin pelican
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b master
git push origin master
git checkout pelican
```
Now you just need to run `publish.bat <commit message>` to make your changes live.



## Modifying your theme