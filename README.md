# Project ideas

Project ideas for Issa Rice. **For the actual ideas, see the [repo issues](https://github.com/riceissa/project-ideas/issues).**

Each issue is a project idea, and should have exactly one effort label, probably one venue label, and at least one format label. (It looks like only repo contributors can edit labels, so you can just explain this in the issue itself.)

Most of the ideas are for me to work on eventually, but others can work on them as well (in fact, I would prefer that since it means less work for me). Others can also add new ideas to this repo for me to work on (similar to [requested answers or "ask to answer" on Quora](https://www.quora.com/What-is-Request-Answers-and-how-does-it-work/answers/11143418)) or comment on existing ideas. In an ideal world, we would all have repos like this one and we could ask each other for specific kinds of output (and the votes and bounties would help us decide what to prioritize).

Some reasons I have this repo are to:

* Give people a better idea of what I might work on next. I like to make myself
  predictable so others can plan according to a good model of how I will act.
* Tell the world the things I want to see. I think the things in this list are
  useful to the world, and it doesn't need to be me who does it. It would be
  great to find out that somebody saw a sufficient need based partly on this
  repo and decided to make something. This is similar to [request for startups](https://www.ycombinator.com/rfs/ "“Requests for Startups”. Y Combinator. September 2016. Retrieved November 26, 2017.") or
  [charities](https://blog.givewell.org/2015/10/15/charities-wed-like-to-see/ "Elie Hassenfeld. “Charities we'd like to see”. GiveWell. March 1, 2017. Retrieved November 26, 2017.").
* Track the things I want to work on. I often think of things I'd like to work on while daydreaming
  or working on something else. If I don't put an effort into recording things
  to work on (and training myself to notice needs that exist in the world), I
  might forget.
* Clean out some tasks from [orgmode](https://issarice.com/emacs). I have a backlog of tasks in orgmode. A
  lot of these aren't for me to immediately work on, and they kind of clutter
  up my orgmode file. If the tasks can be done by somebody that isn't me, why not keep that portion of the todo list public?
* Give potential funders an idea of what they can fund. If I already want to
  see something in the world, a modest amount of funding can shift my
  priorities to work on that thing.  By the way, since I tend to be busy
  with the things I am already working on, it's hard for me to tell whether
  I can actually work on a different thing even given funding, so I would prefer bounties
  that I can claim by completing or making progress on a project
  rather than some sort of pre-commitment to work on a project.
* Find potential collaborators. Especially for the larger projects, it can be
  helpful to have other interested parties on board to divide up the work.
* Give people a better idea of where I'm coming from. This is a broader point
  that applies to other efforts I have made to be more [transparent](https://issarice.com/individual-transparency).

The information in each issue (i.e. project idea) is intended
to be helpful in getting a basic idea of the project, but is only
suggestive; it is often the case that as a project proceeds, details become
clearer or change.

This is not an exhaustive list of project ideas. In particular if I have
already done some work on a project and just want to make general improvements
to it, I won't usually list it here (*all* projects can be improved to varying
extents, and it would be tedious to list them all). If I have specific
improvements, I will try to list them here. If existing projects have their
own GitHub repositories, I will try to add issues there.

**For the actual ideas, see the [repo issues](https://github.com/riceissa/project-ideas/issues).**

## Effort labels

Effort can be rated on the following scale. In each case I assume I am the one
performing the task (skill-sets vary considerably across people so it would be difficult to provide a good estimate for the general population). I have a good programming and writing ability but I am not
exceptional by any means and I expect many people can perform at a comparable
level or even better depending on their expertise. (As a side note, even on the
project idea generation front I don't think I am exceptional – in fact this
repo so far is quite rudimentary and biased toward things I find personally
interesting rather than most useful to the world – so I think other people can
and should also be more transparent about projects they want to see.) Days here
refer to work days, so 8 hour periods. Of course, [planning fallacy](https://en.wikipedia.org/wiki/Planning_fallacy "“Planning fallacy”. English Wikipedia. Retrieved November 26, 2017.") makes it difficult to estimate how long a project will take,
but I list some things I have actually produced in the past to ground myself on
the kinds of tasks and their timescales.

- `low_effort`: Up to one day (8 hours) of effort. These are relatively quick things that can be
done. Examples are [Timeline of Carl Shulman publications](https://timelines.issarice.com/index.php?title=Timeline_of_Carl_Shulman_publications&oldid=15618) as of July 13, 2017 (about 7 hours of work) and some
global health pages like Amanda Glassman (I think).

- `medium_effort`: More than one day and up to two weeks (8–80 hours) of effort. Examples on this level are
[timeline of MIRI](https://timelines.issarice.com/index.php?title=Timeline_of_Machine_Intelligence_Research_Institute&oldid=15715) as of July 15, 2017 (75 hours) at the upper end. I think [timeline of AMF](https://timelines.issarice.com/index.php?title=Timeline_of_Against_Malaria_Foundation&oldid=13553) (33 hours) around the middle.

- `high_effort`: More than two weeks (80 hours) of effort. Examples here are my total work so far on
the [donations list site](https://donations.vipulnaik.com/) (as of November 2017) and my total work on [Devec wiki](https://devec.subwiki.org/wiki/Main_Page) (as of November 2017).

## Downloading issues

To download the issues in this repository, run the script `download_issues.py`
that is included in this repository:

```bash
./download_issues.py
```

This will save the issues as a JSON in `issues.json`. It won't save comments,
but I think the script can be modified to also download comments.

To make sure all the issues were downloaded, you can count the occurrence of a
string that should appear once for each issue, for example:

```bash
grep -F '"title":' issues.json | wc -l
```

## See also

- [Ask me anything](https://github.com/riceissa/ama)

## External links

- [My Quora questions](https://www.quora.com/profile/Issa-Rice/questions "“Issa Rice's Questions”. Quora. Retrieved November 26, 2017.").
  Not all of my questions are "serious" questions, but they are things I
  have wondered about or think others have wondered about, so I would
  appreciate responses.
- [New article pool](https://github.com/vipulnaik/contractwork/blob/master/new-article-pool.mediawiki)
  by Vipul Naik lists article ideas
- Luke Muehlhauser: ["11 Less Wrong Articles I Probably Will Never Have Time to Write"](http://lesswrong.com/lw/85d/11_less_wrong_articles_i_probably_will_never_have/) (2011),
  ["How to study superintelligence strategy"](http://lukemuehlhauser.com/some-studies-which-could-improve-our-strategic-picture-of-superintelligence/) (2014),
  and ["Projects I wish I had time for"](http://lukemuehlhauser.com/projects-i-wish-i-had-time-for/) (2018)
- [orthonormal's 2012 list of posts they would like to write](http://lesswrong.com/lw/cnl/posts_id_like_to_write_includes_poll/)
- [Discussion about research projects people wished others would do, on Raymond Arnold's Facebook wall](https://www.facebook.com/raymond.arnold.5/posts/10215385999617218)
- ["Concrete project lists"](http://effective-altruism.com/ea/18p/concrete_project_lists/) on Effective Altruism Forum
