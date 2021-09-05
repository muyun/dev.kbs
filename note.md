#### note  

#### 2021-09-02  
*  TODO - an application on sharing and storing photos  
    - store my personal photos or videos  
    - historical and rare photographs  
    - art photographs  
    - [Rare Historical Photos](https://rarehistoricalphotos.com/about-us/) 

* Tech side 
    - server with python 
    - frontend with static part, not a framework 

#### 2021-08-30  

* TODO  
    - learn js  

#### 2021-05-15  

* DOM - Document Object Model  

#### 2021-05-06  

* ideas  

  - a tool to track your personal finances 
      + [How you can track your personal finances using Python](https://sgoel.dev/posts/how-you-can-track-your-personal-finances-using-python/)  
      + [plain text accounting](https://plaintextaccounting.org/#plain-text-accounting-apps)  

  - A one-to-one language meetup  

  - A network of microblogs where you can control your content. 
      + NO Ads, NO harassment, and fake news.
      + [microblog](https://micro.blog/)  

  - working in Asyncio  way  
      + [Demystifying Asynchronous Programming in Python](https://chsasank.com/digging-deep-into-async-await-python.html?continueFlag=e55583ffe9198f66eb1db2f897377752)
      + [Asynchronous Everything](http://joeduffyblog.com/2015/11/19/asynchronous-everything/)
  
  -  a network of bookmark or newsletter service  

  -  a blog on 中餐馆  or chinese food  
  
  -  e-commerce ?  
      + [Candide - plants](https://candidegardening.com/GB/identify-plants) 
      + [trogon - learning to identify birds](https://github.com/dandavison/trogon)

  - generative art  

  - personal data management 
      + [SQLite is not a toy database](https://antonz.org/sqlite-is-not-a-toy-database/)
      + [How I store my files](https://www.unixsheikh.com/articles/how-i-store-my-files-and-why-you-should-not-rely-on-fancy-tools-for-backup.html)
  

* build a team  
  + an artisanal crafting team  
      + [SHINY FROG](https://shinyfrog.net/)

* details  
  + begin from Landing page  
      + [Earlyname](https://tinyprojects.dev/projects/earlyname)  
  

#### 2020-08-06 
* issues 
  - fix the markdown format issues  
  to achieve the same with ones from newblog 

  - code highlighting  

* learning  
  - python 
  - react
  - SCSS

#### 2020-03-19  

* issues   
  - the Code/math display on web 
      + jupyter function  ?  - NO, but this is a good way to show the coding result  

      + May adjust the flatpage coding part, using markdown not ReST  
          - [Syntax Highlighting, ReST, Pygments, and Django](http://www.codekoala.com/posts/syntax-highlighting-rest-pygments-and-django/)  

      + use Pygments highlight function  

  -  FIX the front-end issues  

  -  markdown <space> issues 
      +  use ~flask-mistune~ pkg
      + use flask_markdown2 
      +  CHECK MORE, and TO IMPROVE 
      +  rewrite markdown pkg?  

  -  include lines of code 

* deploy  
  -  Deploy [betareader](https://betareader.herokuapp.com/) on heroku  
      + > cd blog  
        > git push heroku master  

* TODO Features 
  -  url_for issue for blueprint 
      +  fixed 
  -  check blueprint and react 
  
  -  next functions  
      +  fix the file format  
         - fix it basically  
      +  on cloud 
         - [mykbs on pythonanywhere](http://muyun.pythonanywhere.com/) 
         - pythonanywhere is for hackers/engineers  
            + cannot support RSS feed from 3rd parties  
         - Deploy [betareader](https://betareader.herokuapp.com/) on heroku  
            

      + tags, Clicking a tag shows all the posts with that tag.
        - DONE   
        - fix the file format issues  
        - tags function is so convenient for index/home functions  
        - so exciting to code it myself 

      +  code optimization and restruct 
        - Done, use filter in back-end, not in front-end/jinja for it

      + Store and list the liked posts and search based on tags
    
      +  A hacker news for some industry  

      + news aggregator or a community
        - RSS feed from new posts or papers  
        - feedparser 

      + write note 
    

      +  only show latest 5 posts, and multi-pages    
        - flask-paginate 

      + TODO 
        - RSS function  - python3-feedgen 
        - a search box that filters the index page by name or date  

      + Q&A interviews 

      + in txt, video format ?  

#### 2020-03-18  

* TODO 
  - react  
  - [markdown in flask](https://florian-dahlitz.de/blog/build-a-markdown-to-html-conversion-pipeline-using-python)
* doc using Sphinx

#### 2020-03-17  

* fix the issue to display books.md 
  + Only get book page in pages 

* improve the frontend  
  + React ?  

* improve flask app 
  + organize server into distince components 
    - add blueprint    
  
* reference
  + [react-flask](http://allynh.com/blog/adding-a-react-frontend-to-your-flask-project/)

#### 2020-03-14  

* TODO  
  + transfer books.md to html 
  + improve the layout  
  + **pytest** 

##### 2020-03-13  

* TODO 
  + design the layout  - fixed, need to improve  
  + pytest functions 

* Fixed 
  + add config_public.py for public setting

##### 2020-03-10  

* TODO  
  + flatpages in Flask  ?  
    - Done 
    - pages Works in jinjia templates, not in Flask 
     

  + pytest functions  
 

* use static not database to manage files
  + flatpages module  
  + sometimes flatpages dones't work in flask  - fix

* React ? 

#### deploy  

* test  
  > pytest  

* run  
  > export FLASK_APP=blog
  > export FLASK_ENV=development  
  > flask run  

##### structure is the key  

* Modules 
  + modular programming - separating code into parts holding related data and function   
  + each module has its **own private symbol table**; 
  thus a module creates a **separate namespace**     
  + import <module_name>  -> only place <module_name> in the caller's symbole table  
  + dir() can find out which names a module defines  

* Packages  

* Test 
  + **what** was done - look at **the result** of a particular behavior   
  + a full **testing suite**  
  + each test unit must be fully **independent**  
  + **write a broken unit test about** what you want to develop next  

* Doc   

#### reference

* [Dead easy yet powerful static website generator with Flask](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)
* [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/writing/structure/)
* [Create a Static Blog Using Python Flask](https://dev.to/arrantate/create-a-static-blog-using-python-flask-1oab) 
* [pythonanywhere](https://www.pythonanywhere.com/user/muyun/)
* [Blask](https://getblask.com/)
