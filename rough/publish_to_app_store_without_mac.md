Title: How to Publish Your Unity Game to the App Store Without a Mac or an iPhone
Date: 2019-08-07 12:00
Modified: 2019-08-07 12:00
Category: Tutorials 
Tags: Game Development 
Slug: publish-to-app-store-without-a-mac
Authors: David Jorna
Summary: Publish to the App Store without while paying Apple the minimum possible amount.
Featured_Image: images/combined.png

One of the benefits of working with a game engine with Unity3D is that you only have to code your game once. This is great for mobile games, as you will usually want to publish your game on both the Google Play store and Apple's App Store. If you really want to cast a wide net, you can also sell your app on Amazon. Then there's the global distribution center [Catapult](https://catappult.io/) which you probably haven't heard of. And if you want to reach the Asian market there's also the MOO Store for Southeast Asia, One Store for Korea, and Xiaomi's Mi Game Center for China.

But let's just stick to the main 2 for now.

## Step 1: Joining the Apple Developer Program

You will need:
* $132 CAD ($99 USD)
* A trustworthy friend with an iPhone

Joining Apple's Developer Program is necessary if you want to deploy you app to the App Store. They also charge you a hefty $99 yearly fee for the privilege of being in their store. This may me a shock to you if you already paid Google's one time developer fee of $50. But if you own a lot of Apple products, you can probably afford it. It's no wonder that [iOS is more popular in richer counties](https://deviceatlas.com/blog/android-v-ios-market-share).

Once you've emotionally prepared to part with your hard-earned money, now comes the tricky part. As of February 27th of 2019, [Apple now requires you to enable two-factor authentication to create a Developer account](https://www.macrumors.com/2019/02/13/developers-two-factor-authentication-required/). This makes your account more secure, but it also means that you'll have a hard time creating an account if you don't own any Apple products. Even using a cloud service, or running macOS in a VM won't work, because you'll have to have access to the device's unique UDID. Even buying a used Mac or iPhone is risky as well, because you can only create a maximum of 3 new accounts on a single machine, which the original user may have done already. This is one of those rare problems that you can't solve from the safe familiarity of your bedroom. **You're going to have to go outside and find a friend.**

If you don't have access to a friend, a colleague or acquaintance will do in a pinch. Ask them to let you borrow their iPhone or Mac, and it shouldn't take more than 15 minutes. All you have to do is sign into their device with your Apple ID, and enable two-factor authentication. You'll also need the UDID of the device, and the login password. It's a bit intrusive, but once you have this set up, you won't have to borrow the phone again. Just make sure you set up two-factor authentication with your phone number and not your friend's.

## Step 2: Building your Game For iOS

If you're running Windows or Linux, you can still build for iOS, but instead of creating a .ipa file, Unity builds an XCode project which can then be build built on a Mac.

However, that's now the way I would suggest you go about it. I'm running macOS in a virtual machine, so my workflow using this method was: build for iOS on Windows, transfer the files to the VM via Google Drive, then build it in the VM. This is a really time consuming and error-prone process. So instead I would suggest you check out Unity Cloud Build. It

## Step 3: Get Access to macOS

In order to publish your app to TestFlight or the App Store, unfortunately you have to use XCode at some points. Without shelling out for a Mac, you have two options: run macOS in a VM or use a cloud service. I tried out both of these, and they're both good options. The one you choose just depends on your priorities and budget. Do you have the time and technical skills to go through the painful process of installing a virtual machine? Then go with the VM. Do you want to save time, and are willing to spend at least $20 per month or $1 per hour on a cloud service? Then go with the cloud. I personally went with the VM because I like the control, but I admit it was a pain to set up. If I knew how long if would take to set up ahead or time, I'd probably just go with the cloud service. I'll go over both options here so you can decide what works for you.

### Option 1: Use a Cloud Service
You can use a service like macincloud.com to get up and running in around 20 minutes. For the purpose of publishing your app, I would probably go with an hourly plan, since you shouldn't take over 20 hours per week uploading your app.

I personally only have experience with macincloud.com, but here are some other options which look promising as well:
1. [wens.io](https://www.wenz.io/ApplicationLoader)  
wens.io offers a service that gives you the only program we actually need, Application Loader, for €9.99 ($11.22 USD or $14.96 CAD) per month. 
2. [App Uploader](http://www.appuploader.net/appuploader/download.php)  
For a $40 / year licensing fee, App Uploader will generate the provisioning profiles and certificates you need, and upload your .ipa file to the App Store. 

Pros:
* Get up and running quickly
* XCode comes pre-installed
  
Cons:
* Costs more than $0

### Option 2: Run macOS in a VM
Your other option is to run macOS in a VM. I used VirtualBox and followed [this tutorial](https://techsviewer.com/install-macos-mojave-vmware-windows/) which includes links to the relevant files. With this route, you can expect to spend several hours downloading the disk image files and creating the VM. You'll also have to install XCode once the VM is ready, so make sure you save enough 

Pros:
* Free
* Full control and ownership over your software

Cons:
* Hours of time that could be spent coding your game, marketing, playing frisbee, etc.
* Could run slowly depending on your hardware


## Step 4: Publishing to TestFlight / the App Store
Now that you have your .ipa file from Unity built, you'll want to publish it to TestFlight for beta testing. I'll just cover publishing to TestFlight here, but publishing to the App Store is a similar process.

