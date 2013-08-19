hcc-packaging
=============

RPM packaging repository for HCC.

This repo provides the specfiles and source references necessary to build
packages for HCC.

HCC uses the [OSG Koji](https://koji-hub.batlab.org/koji/) instance and
the corresponding [osg-build software](https://twiki.grid.iu.edu/bin/view/SoftwareTeam/KojiWorkflow).

For the most part, HCCs usage of these tools mirror OSG.  Below, I note the very basic
steps for configuration, building, and promoting of existing packages.  Creating a new
package is a workflow completely identical to the OSGs.

Prereqs
-------
0.  Make sure you have a valid grid certificate [from the OSG](http://idmanager.opensciencegrid.org).
    This will need to be installed as ~/.globus/usercert.pem and ~/.globus/userkey.pem.
1.  File an [OSG-JIRA ticket](http://jira.opensciencegrid.org/browse/SOFTWARE)
    requesting access to the HCC build repository on the OSG Koji.  You will need
    to add Brian Bockelman as a watcher so he can approve your access.

Setting up your build environment
---------------------------------
0.  Install the OSG repo RPM ([el5](http://repo.grid.iu.edu/osg-el5-release-latest.rpm) or [el6](http://repo.grid.iu.edu/osg-el6-release-latest.rpm)).
1.  Install the osg-build RPM (`yum install osg-build`).  You need version >= 1.2.7 (you may need to `--enablerepo=osg-development`)
2.  Clone the git repo (`git clone git@github.com:unlhcc/hcc-packaging.git`)
3.  Install the basic OSG koji configuration files: `osg-koji setup`.

Building
--------

To build a package named `foo` in Koji, from the hcc-packaging top-level directory:

    osg-build koji --repo=hcc foo

There are quite restrictive rules on building "real" packages - no uncommitted changes
are allowed in the directory and the current branch must be pushed to github.

If you are just testing a package, then you can add `--scratch` to your command-line;
this will relax the extra git rules, but will not result in a package in the yum repo.

Promoting
--------

Builds automatically go to the nebraska-testing repo, not the production repo.  To tag a
package named `foo` into the release repo:

    osg-promote --route hcc foo

This requires `osg-build` version 1.2.8 or later.

