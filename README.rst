============
GconnectApps
============

The master branch of this repository provides a Gconnect standard bare-bones Flask framework. 
Fork this to begin development on GConnect web apps.

    1. Fork to personal.
    2. Rename the project (in Github Settings).
    3. Fork back to the group.
    4. Delete the personal fork.
    
* As you work on your personal site, avoid editing the "core" javascript, css, and templates.
  See the `Developing your own website` section below.

Installation
============
Most likely you do not want to work on this repository directly. Instead, clone the site you are working on,
*GconnectAppSite*

**Step 1:** Clone the repository

   >>> 'git clone https://github.com/gconnectAfrika/schoolmanager.git' _
   >>> cd schoolmanager 
   
**Step 2:**  Checkout to the required branch where your project is
	>>> git branch yong
	>>> git branch checkout yong 
	
**Step3:** Create a virtual environment, activate it, install dependencies. Note, make sure you are using
   virtualenv see `https://realpython.com/blog/python/python-virtual-environments-a-primer/`
   and `http://stackoverflow.com/questions/29950300/what-is-the-relationship-between-virtualenv-and-pyenv`
   for a brief description. If the virtualenv library is not installed the virtual environment, the venv
   that gets included will include site-packages from the system-wide location.
   From a shell within the cloned location GconnectAppSite

   >>> pip install virtualenv
   >>> python -m venv .
   >>> .\Scripts\activate.ps1
   >>> python -m pip install --upgrade pip
   >>> pip install -r requirements.txt

   if pip fails with an SSLError, on Windows you can create %APPDATA%\\pip\\pip.ini with the content::
   
   .. note::
   
      This might not work because of Artifcatory or SSH authentication issues. If you get any errors inline with this
      use the following to by-pass that.
   
   >>> pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org

   
**Step4:** Start the service

   >>> python run.py
   

	.. note::
	   If the environment you are working in doesn't have internet access, do the above steps (up to 3)
	   from a computer that does and run.
	   if there is no dependencies folder, make a new directory
	   >>> mkdir dependencies
	   Download dependencies from the internet or check if dependencies are already installed.
	   >>> pip download --dest "./dependencies" -r requirements.txt 
	   Install packages from the dependencies folder
	   >>> pip install --no-index --find-links="./dependencies" -r requirements.txt 


Developing your own website
===========================
You really shouldn't be developing in the GconnectApps repository. It is fairly locked down, with pull requests requiring multiple approvals.

Instead, you should have forked the GconnectApps repository to your own. That said, you still want to benefit from development that is 
happening within the GconnectApps repository. To facilitate this, and to ease the sharing of code,
we recommend setting up a 'GconnectApps' remote branch immediately (see step 1 below).

Git accommodates many workflows, but our recommended workflow is as seen below.


Incorporating GconnectApps updates into the fork
================================================

1. add schoolmanager as a remote repository:

   >>> git remote add schoolmanager https://github.com/gconnectAfrika/schoolmanager.git   _

2. to update from the branchA on schoolmanager to branchB in your repository (assuming they exist)

   **Method 1:**
   
   >>> git checkout branchB
   >>> git fetch schoolmanager
   >>> git merge schoolmanager/branchA
   
   **Method 2:**
   
   >>> git checkout branchB
   >>> git fetch schoolmanager
   >>> git rebase schoolmanager/branchA
   
   **Method 3:** (specific files or folders)
   
   >>> git fetch schoolmanager
   >>> git checkout schoolmanager/master -- folder/file.ex (folder/ works too)


Pushing your development back to schoolmanager
==============================================

As above, set the master branch to track schoolmanager:

   >>>  git remote add schoolmanager 'https://github.com/gconnectAfrika/schoolmanager.git ' _


If, for instance, you want to update the "core" file core-X

   >>> git fetch schoolmanager
   >>> git checkout schoolmanager/master
   >>> git checkout master core-X
   >>> git commit
   >>> git push schoolmanager 

The code structure provides 'static/css/schoolmanager-sitecustom.css' and 'static/js/schoolmanager-sitecustom.js',
and you should try and put your custom code here, not in 'schoolmanager.css' or 'schoolmanager.js'.

This stackoverflow question has some great examples of workflow with remote and local branches:
'http://stackoverflow.com/questions/11266478/git-add-remote-branch' _

Creating a remote called "my_remote":

   >>> git remote add my_remote 'git://github.com/jdoe/coolapp.git' _
   >>> git fetch my_remote

List all remote branches:

   >>> git branch -r
   
Create a new local branch (test) from a my_remote remote branch (pu):

   >>> git branch test my_remote/pu
   >>> git checkout test
   
Merge changes from my_remote's remote branch (pu) with local branch (test):

   >>> git fetch my_remote
   >>> git checkout test
   >>> git merge my_remote/pu

Update my_remote's remote branch (pu) from a local branch (test):

   >>> git push my_remote test:pu

Creating a new branch on a remote uses the same syntax as updating a remote branch. For example, create new remote branch (beta) on my_remote from local branch (test):

   >>> git push my_remote test:beta
   
Delete remote branch (pu) from my_remote:

   >>> git push my_remote :pu

Editing sidebar/collapsed-navbar links
======================================

Your sidebar links automatically shift into the navbar dropdown menu when the browser becomes narrow. Because this requires populating more than one template with the same set of links, we store the links in a list called SIDEBAR_LINKS in config.py. Before each request, SIDEBAR_LINKS is copied to g.sidebar_links. If anything needs to be dynamically added, do so after this step in before_request(). Each entry in SIDEBAR_LINKS is a dictionary with the following entries:

* **label** *(string)*: The link text, what appears between the <a></a> tags.
* **href** *(string)*: The link destination, what appears after href=, or in url_for().
* **is_view_name** *(boolean)*: False if href is a URL (absolute or relative), True if href is a view name that should be expanded with url_for(). 
* **nested** *(list)*: Empty list if there are no links nested below this one, otherwise a list of dictionaries structured exactly like this one (but without a 'nested' entry).
