# Contributing

Apart from the below guidelines, you should be familiar with GIT, GitHub, 
GNU Make and BASH scripting and also the (programming) languages, platforms,
frameworks, and language specific toolings used by this project.

If you want to report a bug or issue a feature request, you might want to
skip to either

* [Reporting Bugs](CONTRIBUTING.md#reporting-bugs)
* [Requesting Features](CONTRIBUTING.md#requesting-features)


## Release Management

We expect that we will be releasing at most four minor release versions per
year, not including any in-between maintenance release versions.

Example:

* `1.0.0` (Q1)
* `1.1.0` (Q2)
* `1.2.0` (Q3)
* `1.3.0` (Q4)

New minor releases will be made available at around the end of each quarter.
This also includes new major releases that break overall compatibility.

However, and for as long as there are no new features to be implemented, we will
disband that schedule.


### Support Policy

We will support at most three minor release versions including the current
release version. For these we will provide maintenance releases.

Example:

* `1.4.x` (not supported)
* `1.5.x` (supported)
* `1.6.x` (supported)
* `2.0.x` (current, supported)

That being said, and if you happen to be using an older version of the software,
you are strongly advised to migrate to the most recent release version.


### Release Tags

For release tags we use the standard semantic versioning scheme, where we have
a major release number, a minor feature release number, and, a maintencance
version number, e.g. `releases/0.0.1`.

The general pattern for all release tags is `releases/<release-version>`.

For historical purposes, all release tags will be kept in the repository and
must never be deleted.


#### Major Release Number

A change in the major release number indicates a breaking change that will break
backward compatibility.


#### Minor Feature Release Number

Minor feature release number changes indicate new features that are backward
compatible.


#### Maintenance Version Number

Changes in the maintenance version number indicate bug fixes or non breaking
refactorings.


#### Development Release Tags

During pre/alpha development, we will provide snapshot releases from the
existing feature integration branches, e.g. `releases/0.2.0.dev1`. These
snapshots can then be used for early integration by dependent other projects.

The general pattern for all development release tags is 
`releases/<future-major-or-minor-release-version>.dev<dev-release-number>`.

The `dev-release-number` will be incremented by one on each release and it
starts at `1`.

In order to create such a branch, simply run

```
> git checkout -b releases/<future-major-or-minor-release-version>.dev<dev-release-number>
```

Side Note: Python uses `.dev<N>` for denoting development releases. Since we
use Python, we will stick to that convention, as it is well proven, regardless
of any other platform or tooling that we might use.


#### Release Candidate Tags

When finalizing a feature release during beta development, we will provide
snapshot release candidates from the existing feature integration branches,
e.g. `releases/0.1.0rc1`.

The general pattern for all release candidate tags is 
`releases/<future-major-or-minor-release-version>rc<rc-release-number>`.

The `rc-release-number` will be incremented on each release and starts at `1`.

In order to create such a tag from the feature integration branch, simply run

```
> git tag releases/<future-major-or-minor-release-version>rc<rc-release-number>
```


#### Stable Release Tags

Once a feature integration branch that is scheduled for being the next release
becomes stable, we will merge it into the master branch and then tag that as the
next stable release.

```
> git tag releases/<next-stable-release-version>
```

The same holds true for maintenance integration branches. In this case, however,
we might not always be able to merge these into the master branch. In this
situation we will create the release tag directly from the integration branch.

```
> git checkout integration/...
> ...
> git tag releases/<next-maintenance-release-version>
```


## Reporting Bugs

First, please use the provided template and provide us with the requested
information.

If we find that two or more bugs are intertwined and depend on each other, we
will merge them into a combined new bug report.


### How we Process Bug Reports

Once we have confirmed that the bug still exists in the [currently supported releases](CONTRIBUTING.md#support-policy),
we will accept it and provide maintenance releases for these as soon
as possible.

If we cannot confirm the bug in any of the supported releases, we will post
the following comment and then close the issue.

```
Unable to confirm. Issue has been fixed since releases/<release-version>.
Closing.
```

Otherwise, we will continue processing the bug using the following workflow. 

1. We will create a maintenance branch for the least recent minor release still
being supported and for which the bug was confirmed.

```
> git checkout -b maintenance/<release-version>/<bug-issue-number> releases/<release-version>
```

2. We will then post a comment which tells us/you the branch against which all
pull requests must be made against.

```
Bug confirmed in the following releases:

* <release-version-x>
* <release-version-y>
* <release-version-z>

Maintenance branch maintenance/<release-version>/<issue-number> created.

All pull requests regarding this issue must be made against this branch only.
```

3. We or you start fixing the bug (including required test cases) for that
release and make pull requests against the maintenance branch.

4. Once the bug was fixed for that release, we will begin to forward port the
bug fix to the remaining two release versions still under support, again 
creating maintenance branches for these releases.

5. Dependening on the severity of the bug, we will either schedule it for a
cumulative maintenance release or directly make a maintenance release from it.


### Making Pull Requests

Per maintenance branch, all of the bugs that are mentioned by the respective
issue must be fixed.

* Side Effect Free

  Apart from fixing existing bugs, all maintenance work must be free of any side
  effects.

* Non Breaking Refactoring

  Maintenance branches must not include any breaking refactorings so that they
  remain free of any side effects in regard to dependent other projects.

* Well Tested

  See [Testing](/CONTRIBUTING.md#testing) below.

If your pull request does not meet these requirements, it will be rejected.


## Requesting Features

First, please use the provided template and provide us with the requested
information.

All feature requests must be made against the most recent release version.


### How we Process Feature Requests 

TBD


### Making Pull Requests

TBD


## Branching Policies


### Stable Master Policy

The master branch must always be stable and reflects the most recent, stable,
release of the project.


### Maintenance Branches

All maintenance development must occur inside maintenance branches.

The prefix for all maintenance branches must be `maintenance/<release-version>`.


### Feature Branches

New features must be developed inside feature branches. Per feature branch, a
single new feature must be developed.

The prefix for all feature branches must be `features/`.

Feature development must always be made against a branch derived directly from
the master branch and changes to that master branch must always be merged into
the feature branch on a frequent basis.

* Side Effect Free

  Features must be side effect free, i.e. existing and newly developed features
  must not be broken and dependent other projects must continue to work.

* Non Breaking Refactoring

  Feature branches must not include any breaking refactorings so that they
  remain free of any side effects in regard to existing dependent other
  projects and other features currently in development.

* Well Tested

  See [Testing](/CONTRIBUTING.md#testing) below.

In order to create a feature branch, simply run

```
> git checkout -b features/<feature-issue-number> master
```


### Feature Integration Branches

When preparing for a new major or minor release, one or multiple feature
branches will be combined into an integration branch.

Issues that arise during the integration must be fixed inside the feature
branches and will then be merged back into the integration branch.

The branch name for all feature integration branches must be based on the
following template: `integration/future-major-or-minor-release-version>`

```
> git checkout -b integration/<future-major-or-minor-release-version> master
```

From these integration branches we will create release candidate tags which
can then be used for further testing.

Once the release becomes stable, we will merge the integration branch to master
and tag it as a stable release.

The integration branch along with all integrated feature branches will then be
deleted.


### Maintenance Integration Branches

In order to prepare a maintenance release, one or multiple maintenance branches
will be combined into an integration branch.

Issues that arise during the integration must be fixed inside the maintenance 
branches and will then be merged back into the integration branch.

The branch name for all maintenance integration branches must be based on the
following template: `integration/<future-maintenance-release-version>`.

```
> git checkout -b integration/<future-maintenance-release-version> <branch-or-release-tag>
```

From maintenance integration branches, we will never create any release
candidates nor development releases.

Once the release becomes stable, we will merge the integration branch to master
and tag it as a stable release.

The integration branch along with all integrated maintenance branches will then
be deleted.


### Refactoring Branches

For the purpose of (overall) refactoring, refactoring branches will be created.
During refactoring, all feature development will be put to a halt.

Refactorings that affect dependent other projects require refactoring branches
in these projects as well.

The branch name for all refactoring branches must be based on the following
template: `refactoring/<current release version>/<future release version>`.

* Well Tested

  See [Testing](/CONTRIBUTING.md#testing) below.


## Testing

Testing these kind of projects is rather difficult and for now we will resort
to manual testing only.
