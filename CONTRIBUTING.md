# Contribute to GFAST web apps


Thank you for your interest in GFAST web apps. 
The guide below outlines the best way to contribute. 



## Development and merge requests



1. Create a separate branch off master
2. Write code and tests
3. Make sure to document your code following the numpydoc style, 
   https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
3. Check your code style with every commit by  incorporating Flake8 and githooks webhooks in your local development.
   See README on how to install Flake8 and enable webhooks
5. Commits squashing 
    * It can be difficult to review more than few commits. Please consider squashing 
      them into few logically organized and clear messages. https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#Squashing-Commits
6. Push the code to your fork and not the master brach 
7. When ready to submit a merge request, make sure the merge request is clear on :
    * The MR title should describe the change you want to make
    * The MR description should give a motive for your change and the method you
used to achieve it.

    Mention the issue(s) your merge request solves, using the Solves #XXX or
    Closes #XXX syntax to auto-close the issue(s) once the merge request will
    be merged.
8. Set labels


## Submitting issues


When submitting new issues, use labels. See workflow labels. 

## Workflow labels


Using labels enables us to set priorities and organize the workflow. 
GitLab team already has well defined workflow labels in their contribution guide and 
below is an outline of their approach we have adopted as well: 

Most issues will have labels for at least one of the following:

* Type: feature, bug, nice-to-have, architecture decision etc. 
* Subject: this defines the area such as frontend, backend, concourse, artifactory, etc. 
* Priority: use "priority" label to mark important issues

* Adding new labels:
    
    Labels are something we are stil incorporating into our workflow and some guidelines might change in the future, but for now:
    * You will find most of the workflow labels are already defined on the Gitlab Group level. 
      Unless the new label that is required is very specific to your project, please push the label to group level. 
    * Before adding a new label, review that the label is not already present or perhaps the current one needs improvement. 


## Style Guide

 * Python: 
    * numpydoc
 * Markdown:  
    * Google: https://github.com/google/styleguide/blob/3591b2e540cbcb07423e02d20eee482165776603/docguide/style.md
   (At the momenent, this is a consideration too https://github.com/cirosantilli/markdown-style-guide/blob/gh-pages/index.md ) 
