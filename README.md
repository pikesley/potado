[![Build Status](http://img.shields.io/travis/pikesley/potado.svg?style=flat-square)](https://travis-ci.org/pikesley/potado)

# Potado

_A robot to simplify setting the [Tado](https://www.tado.com/gb/) heating schedule_

We've had a Tado [smart thermostat](https://www.tado.com/gb/products/smart-thermostat-starter-kit) for a couple of years, but we recently got some of the [radiator robots](https://www.tado.com/gb/products/smart-radiator-starter-kit) which means setting the schedule(s) is now a lot more tedious. So, I made this

## Using it

It's easiest to run it as a Docker container. So:

```
git clone https://github.com/pikesley/potado
cd potado
make build
```

### Credentials

To do anything useful, you need to

```
cp potado/conf/credentials-example.yaml potado/conf/credentials.yaml
```

and fill in your Tado username, password, and client secret (which doesn't seem to change and can be found [here](https://my.tado.com/webapp/env.js))

At this point, you have three choices:

### Prepare the default schedules

All of this relies on you having set up the Tado [Zones](https://community.tado.com/en-gb/discussion/859/create-zones) when your equipment was being fitted. Presuming this is true, then running

```
make init
```

will fire up the Docker container, gather up your zone names, and dump a dummy schedule at `potado/conf/schedule-default.yaml`. Note that this is a _terrible schedule_ and I don't recommend applying it as-is, but it provides a good starting-point. Presuming you're starting from scratch, then

```
cp potado/conf/schedule-default.yaml potado/conf/schedule.yaml
```

and fill it in. The `potado/conf/schedule-example.yaml` file has some comments in it which might help

### Apply the schedules

Once you've got the schedules set up the way you want, then to actually set them, do

```
make schedule
```

### Get on the container

If you want to run the tests or something, then try

```
make run
```

to get a shell on the container (with `potado` mounted at `/opt/potado)

Then do

```
make
```

to run the tests

## Tado's API

I've made some Choices here. In particular I've assumed that we want the same schedule on each weekday, then probably something different on the weekend, which fits with Tado's `THREE_DAY` timetable type (which recognises `MONDAY_TO_FRIDAY`, `SATURDAY` and `SUNDAY`). All together, Potado supports

* `mon-fri`
* `saturday`
* `sunday`
* `weekend` (expands to `saturday` and `sunday`)
* `all` (expands to `mon-fri`, `saturday` and `sunday`)

See `potado/conf/schedule-example.yaml` for more on this. It shouldn't be too hard to support the two other timetable types (`ONE_DAY` and `SEVEN_DAY`) if anybody wants to have a crack at some Python

In general, the API seems to be powerful but very undocumented. I am eternally grateful to [Terence Eden](https://shkspr.mobi/blog/2019/02/tado-api-guide-updated-for-2019/) and [Stephen Phillips](http://blog.scphillips.com/posts/2017/01/the-tado-api-v2/) for working out at least some of how this all works

## Why have you done this?

Have you met me? Also, because trying to set such a large number of schedules on the fiddly little mobile app is awful. And as an excuse to learn some better Python testing techniques

I realise that some people would rather set the schedule by spending time clicking backwards and forwards on the Tado phone app than deal with YAML. Sorry

## At this point, wouldn't it have been quicker to just suck it up and set the schedules on the app?

Yes. Yes it would
