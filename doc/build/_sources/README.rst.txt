========
ManuApps
========

The master branch of this repository provides a GFAST standard bare-bones Flask framework. 
Fork this to begin development on Manulife web apps.

* Gitlab does not currently allow the forking of a Group project to a project within the same Group
    (https://gitlab.com/gitlab-org/gitlab-ce/issues/17358). Instead
   
    1. Fork to personal.
    2. Rename the project (in GitLab Settings).
    3. Fork back to the group.
    4. Delete the personal fork.
    
* As you work on your personal site, avoid editing the "core" javascript, css, and templates.  See the 
  `Developing your own website` section below.

Installation
------------
Most likely you do not want to work on this repository directly. Instead, clone the site you are working on,
*MyManuAppSite*

**Step 1:** Clone the repository

   >>> 'git clone https://gitlab.manulife.com/GFAST/*MyManuAppSite*.git MyManuAppSite' _
   >>> cd MyManuAppSite
   
**Step 2:**  Checkout to the required branch where your project is
	>>> git branch checkout DevProj
	
**Step3:** Create a virtual environment, activate it, install dependencies. Note, make sure you are using
   virtualenv see `https://realpython.com/blog/python/python-virtual-environments-a-primer/`
   and `http://stackoverflow.com/questions/29950300/what-is-the-relationship-between-virtualenv-and-pyenv`
   for a brief description. If the virtualenv library is not installed the virtual environment, the venv
   that gets included will include site-packages from the system-wide location.
   From a shell within the cloned location MyManuAppSite

   >>> pip install virtualenv
   >>> python -m venv .
   >>> .\Scripts\activate.ps1
   >>> python -m pip install --upgrade pip
   >>> pip install -r requirements.txt
   
   :: Note: This might not work because of Artifcatory or SSH authentication issues. If you get any errors inline with this
   use the following to by-pass that.
   
   >>> pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org

**Step4:** We optionally use pywin32 for authenticating against Active Directory. If you will not be using the LDAP authentication, download the appropriate version from https://sourceforge.net/projects/pywin32/files/pywin32/. Pip in a virtual environment cannot install binaries, so use easy_install. To install:

   >>> easy_install pywin32-220.win-amd64-py3.5.exe (or the appropriate file)
    
**Step5:** Start the service

   >>> python run.py
   

	.. note::
	   If the environment you are working in doesn't have internet access, do the above steps (up to 3)
	   from a computer that does and run.
	   >>> mkdir dependencies
	   >>> cd dependencies
	   >>> pip install -r requirements.txt --download="./dependencies"
	   You might want to try this if you get errors.
	   >>> pip download -r requirements.txt
	   Then copy those wheels, zips, and tarballs over to your working environment.


Developing your own website
===========================
You really shouldn't be developing in the ManuApps repository. It is fairly locked down, with pull requests requiring multiple approvals.

Instead, you should have forked the ManuApps repository to your own. That said, you still want to benefit from development that is 
happening within the ManuApps repository. To facilitate this, and to ease the sharing of code,
we recommend setting up a 'manuapps' remote branch immediately (see step 1 below).

Git accommodates many workflows, but our recommended workflow is:

Incorporating ManuApps updates into the fork
--------------------------------------------
   
1. add ManuApps as a remote repository:

   >>> git remote add manuapps 'https://gitlab.manulife.com/GFAST/ManuApps.git' _

2. to update from the branchA on ManuApps to branchB in your repository (assuming they exist):

   ** Method 1:**
   
   >>> git checkout branchB
   >>> git fetch manuapps
   >>> git merge manuapps/branchA
   
   ** Method 2:**
   
   >>> git checkout branchB
   >>> git fetch manuapps
   >>> git rebase manuapps/branchA
   
   ** Method 3:** (specific files or folders)
   
   >>> git fetch manuapps
   >>> git checkout manuapps/master -- folder/file.ex (folder/ works too)


Pushing your development back to ManuApps:
------------------------------------------

As above, set the master branch to track Manuapps:

   >>> git remote add manuapps 'https://gitlab.manulife.com/GFAST/ManuApps.git' _

You really only want to push files that have changes to the core of the website, not the site-specific changes.
Cherry pick these changes, or merge individual files.
Here is a good explanation 'http://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch' _

If, for instance, you want to update the "core" file core-X

   >>> git fetch manuapps
   >>> git checkout manuapps/master
   >>> git checkout master core-X
   >>> git commit
   >>> git push manuapps 

The code structure provides 'static/css/gfast-sitecustom.css' and 'static/js/gfast-sitecustom.js',
and you should try and put your custom code here, not in 'gfast.css' or 'gfast.js'.

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

Editing sidebar/collapsed-navbar links:
---------------------------------------

Your sidebar links automatically shift into the navbar dropdown menu when the browser becomes narrow. Because this requires populating more than one template with the same set of links, we store the links in a list called SIDEBAR_LINKS in config.py. Before each request, SIDEBAR_LINKS is copied to g.sidebar_links. If anything needs to be dynamically added, do so after this step in before_request(). Each entry in SIDEBAR_LINKS is a dictionary with the following entries:

* **label** *(string)*: The link text, what appears between the <a></a> tags.
* **href** *(string)*: The link destination, what appears after href=, or in url_for().
* **is_view_name** *(boolean)*: False if href is a URL (absolute or relative), True if href is a view name that should be expanded with url_for(). 
* **nested** *(list)*: Empty list if there are no links nested below this one, otherwise a list of dictionaries structured exactly like this one (but without a 'nested' entry).

Using Flask-Admin:
------------------

To simplify managing your database models, Flask-Admin is included. This automatically generates an /admin view allowing you to see and edit the content of your database. Note, however, that unless you add special security to handle admin access in production, **you should set CREATE_ADMIN_VIEWS to False in config.py before pushing to production**.

The basic process is simple. For each model (eg, User, ModelName) defined in models.py, add an admin.add_view line in views.py:

.. code-block:: python

   # --- Add admin ModelViews here --- #
   admin.add_view(MyModelView(User, db.session))
   admin.add_view(MyModelView(ModelName, db.session))
   # --------------------------------- #

These will then be accessible via /admin in your application. You can also edit templates/admin/index.html to change the content of the base /admin page.

Lots of information on how to customize the admin views, including limiting which model fields can be seen or edited, can be found at http://flask-admin.readthedocs.io/en/latest/.


Running on Pivotal Cloud Foundry
================================
* GSD maintains a quick guide to PCF/Git within MFC (including setting sslVerify to false):
  https://gitlab.manulife.com/DevOpsTechInfo/help-pcf
  https://gitlab.manulife.com/DevOpsTechInfo/help-git
  
Follow the 15 minute guide here:
* https://pivotal.io/platform/pcf-tutorials/getting-started-with-pivotal-cloud-foundry/deploy-the-sample-app

run the CF installer, in the included zip. This install the commandline tools needed to interact with PCF.

MFC's PCF portal is found here:

* https://login.sys.dev.gsdcf.manulife.com/login

  MFC's login endpoint for PCF has changed recently to
  https://api.sys.dev.gsdcf.manulife.com

  >>> cf login https://api.sys.cac.preview.pcf.manulife.com

  GFAST development is done in org is 'GSD-CAC-DEV', Space 'GFAST-CAC-DEV'

  The full login command is:

  >>> cf login https://api.sys.cac.preview.pcf.manulife.com -u <lan id> -p <password> -o GSD-CAC-DEV -s GFAST-CAC-DEV

  You can check which ORGS/Spaces you have access to by logging in the Pivotal Application Manager `https://login.sys.cac.preview.pcf.manulife.com/login`

* edit the manifest.yml, changing the name of the application
  
* On first run, create the database. Note, we had issues installing pyodbc (requires unixodbc driver),
  so we switched to the python-conda buildpack instead of the default python (pip-based) one
  (this hasn't helped either: https://github.com/cloudfoundry/python-buildpack/issues/34)

  cf push manuapps -c "python db_create.py" -b https://github.com/ihuston/python-conda-buildpack.git
  cf push manuapps -b https://github.com/ihuston/python-conda-buildpack.git
  
* To migrate your project into the production PCF area, you need to set up a concourse pipeline. This process is defined here:
  https://gitlab.manulife.com/geesoffice/onboarding-template

  Once you fill in these templates/forms, then email the GSD engineering team.


Connecting to SQL
=================

https://gitlab.manulife.com/GEES/azure-service-broker/tree/master/azure-sql-db

* List available services::

    cf marketplace

* Create a service instance, I'll leverage azure-sqldb. Copy the template SQL config file, adjust the password::
    
    cp CF_sqldb_nonprod_eastus.json.template CF_sqldb_nonprod_eastus.json
    cf create-service azure-sqldb basic azuresqldb -c CF_sqldb_nonprod_eastus.json

** Note::

  I could not get Python to connect to SQL server when deploying on linux nodes. There were issues compiling pyodbc on linux, Cloud Foundry does not provide the unixodbc driver.

# Bind the service to the app

   cf bind-service manuapps azuresqldb
   cf restage manuapps
   
# you can see the SQL credentials by typing

   cf env manuapps

* use mysql instead::

   >>> cf create-service p-mysql 5GB-dev mysqldb
   >>> cf bind-service manuapps mysqldb


# adjust the database parameters in config.py, use 'cf env manuapps' to find the credentials

   * change USE_SQLITE = False
   * fill in the server, port, database, uid, pwd, as listed by 'cf env manuapps'
	 >>> cf push manuapps -c "python db_create.py"
     >>> cf push manuapps


Other Pivotal tips
------------------
* delete a route
  >>> cf routes
  >>> cf delete-route apps.dev.gsdcf.manulife.com --hostname X


concourse
---------
Concourse is Pivotal's continuous integration tool.
The provisioning pipeline is defined in the 'concourse' subfolder.

Note: Currently missing development branch

* Edit the *concourse-credentials.yml* file in the concourse subfolder.
  Specifically, change the *private key* (be sure to upload the public key
  to gitlab), change the *git_uri* to your repository, and adjust *app_name*.

We have created a GFAST deploy key, stored the private key in cyberark
(as well as the credentials file). See  
`https://mlisgciscybws1.americas.manulife.net/PasswordVault/logon.aspx?ReturnUrl=%2fPasswordVault%2fdefault.aspx`
for cyberark login. See `https://gitlab.manulife.com/help/ssh/README`
for a description of Deploy Keys. You should be able to leverage this key
across all GFAST web apps. Select Deploy Keys in your project's settings
and enable the GFASTConcourse key. 

To provision within the DEV foundation, log in and set your target (Note, these
steps are in the 'concourse/nonprod/updatePipeline.sh' file, but I prefer
to run these commands explicitly). Logging in should only need to be done once
(u: admin, p: G$dc0ncourse). 

   fly --target manulife-ci login --concourse-url https://concourse.sys.dev.gsdcf.manulife.com --insecure

Adjust manuapps to your application's name (edit and run updatePipeline.sh, or type the commands directly):

   fly -t manulife-ci set-pipeline -c pipeline.yml -p manuapps-poc-dev-ci --var app_name=manuapps-poc-dev-ci -n -l ../concourse-credentials.yml

   fly -t manulife-ci unpause-pipeline -p manuapps-poc-dev-ci
  
You can see your pipeline by surfing to `gfast pipeline <http://concourse.sys.dev.gsdcf.manulife.com>` _
For now, log in the "main" team and use the admin credentials listed above.

   
Get the list of available docker images

curl https://10.234.24.211/v2/_catalog -k

testing on dev:
edit updatePipeline.sh set

update concourse-credentials.yml

fly targets
https://concourse.ci/fly-login.html
fly -t manulife-ci login -c https://concourse.sys.dev.gsdcf.manulife.com
username: admin
password: G$dc0ncourse


