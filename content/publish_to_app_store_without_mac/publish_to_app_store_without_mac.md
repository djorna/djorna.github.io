Title: How to Publish Your Unity Game to the App Store Without a Mac or an iPhone
Date: 2019-08-07 12:00
Modified: 2019-08-08 21:25
Category: Tutorials 
Tags: Game Development 
Slug: publish-to-app-store-without-a-mac
Authors: David Jorna
Summary: Publish to the App Store without while paying Apple the minimum possible amount.
Featured_Image: /images/to_app_store.png

I recently released the beta of my first mobile game, [Juggl](https://getjuggl.com), for both Android an iOS. Not owning any Apple products besides an old iPod Nano, I found publishing to the App Store to be more difficult than I expected. It's no wonder some indie devs neglect the App Store altogether to save themselves the headache of getting through Apple's strict hardware requirements. 

This is unfortunate, because they're missing out on a lot of potential revenue. Even though [Android has the largest market share globally](https://www.idc.com/promo/smartphone-market-share/os) at around 87%, [iPhone users tend to have deeper pockets and play more games](https://www.mactrast.com/2011/07/iphone-users-pay-more-and-play-more-than-users-of-other-platforms/). Plus, if you're living in Canada, the U.S., Australia, or the U.K., you probably have some friends with iPhones who will want to try out your game, and that's as good a reason as any.

One of the benefits of working with a game engine like Unity3D is that you only have to code your game once. This is great for mobile games, as you will usually want to publish your game on both Google Play store and the App Store. However, don't underestimate the additional work required to publish your mobile game on two stores at once. There's a lot of red tape involved, and Apple has really tried their best to make it impossible to develop for iOS without buying their products.

If you're in a similar situation as me, and you don't feel like buying a Mac and iPhone just to publish your game on the App Store, hopefully I can save you some time with this blog post.

## Step 1: Joining the Apple Developer Program

**You will need:**

* $132 CAD ($99 USD)
* A trustworthy (and trusting) friend with an iPhone

Joining Apple's Developer Program is necessary if you want to deploy you app to the App Store. They also charge you a hefty $99 yearly fee for the privilege of being in their store. This may me a shock to you if you already paid Google's one time developer fee of $50. But if you own a lot of Apple products, you can probably afford it. It's no wonder that [iOS is more popular in richer counties](https://deviceatlas.com/blog/android-v-ios-market-share).

Once you've emotionally prepared to part with your hard-earned money, now comes the tricky part. As of February 27th of 2019, [Apple now requires you to enable two-factor authentication to create a Developer account](https://www.macrumors.com/2019/02/13/developers-two-factor-authentication-required/). This makes your account more secure, but it also means that you'll have a hard time creating an account if you don't own any Apple products. Even using a cloud service, or running macOS in a VM won't work, because you'll have to have access to the device's unique UDID. Buying a used Mac or iPhone is risky as well, because you can only create a maximum of 3 new accounts on a single machine, which the original user may have done already. This is one of those rare problems that you can't solve from the safe familiarity of your bedroom. 

For this next part, you're going to have to find a friend with an iPhone. If you don't have access to a friend, a colleague or acquaintance will do in a pinch. Ask them to let you borrow their iPhone or Mac, and it shouldn't take more than 15 minutes. All you have to do is sign into their device with your Apple ID, and enable two-factor authentication. Also, make sure to write down the login password for their phone. Apple will ask you for it later. Once you have this set up, you won't have to borrow the phone again. Just make sure you set up two-factor authentication with your phone number and not your friend's.

Ideally, you would test your build on a physical device before releasing to open beta. If you have long-term access to an iOS device, you'll also want to write down the [UDID of the friend's device](http://whatsmyudid.com/). However, the basic premise of this tutorial is assuming you don't have access to an iOS device. As a compromise, you may want to make a second testing group that only includes people you know personally, so they can alert you to any major bugs.

***Note**: Borrowing an iPhone is by no means a long-term solution. If you want to start a game development company, or plan to do long-term iOS development, you should probably invest in a Mac and an iPhone for development. Only use this method if you're looking for a short-term way to publish your app as soon as possible with minimal investment.*

## Step 2: Get Access to macOS

In order to publish your app to TestFlight or the App Store, unfortunately you have to use XCode at some point. Without shelling out for a Mac, you have two options: run macOS in a VM or use a cloud service. I tried out both of these, and they're both good options. The one you choose just depends on your priorities and budget. Do you have the time and technical skills to go through the painful process of installing a virtual machine? Then go with the VM. Do you want to save time, and are willing to spend at least $20 per month or $1 per hour on a cloud service? Then go with the cloud. I personally went with the VM because I like the control, but I admit it was a pain to set up. If I knew how long if would take to set up ahead or time, I'd probably just go with the cloud service. I'll go over both options here so you can decide what works for you.

### Option A: Use a Cloud Service
You can use a service like [macincloud.com](https://www.macincloud.com/) to get up and running in around 20 minutes. For the purpose of publishing your app, I would probably go with an hourly plan, since you shouldn't take over 20 hours per week uploading your app.

I personally only have experience with [macincloud.com](https://www.macincloud.com/), but here are some other options which look promising as well:

**1. [wens.io](https://www.wenz.io/ApplicationLoader)**  

  * wens.io offers a service that gives you the only program we actually need, Application Loader, for €9.99 ($11.22 USD or $14.96 CAD) per month. 

**2. [App Uploader](http://www.appuploader.net/appuploader/download.php)**  

  * For a $40 / year licensing fee, App Uploader will generate the provisioning profiles and certificates you need, and upload your .ipa file to the App Store. 

**Pros:**

* Get up and running quickly  
* XCode comes pre-installed
  
**Cons:**  

* Costs more than $0

### Option B: Run macOS in a VM
Your other option is to run macOS in a VM. I used VirtualBox and followed [this tutorial](https://techsviewer.com/install-macos-mojave-vmware-windows/) which includes links to the relevant files. With this route, you can expect to spend several hours downloading the disk image files and creating the VM. You'll also have to install XCode once the VM is ready, so make sure you save enough 

**Pros:**  

* Free  
* Full control and ownership over your software

**Cons:**  

* Hours of time that could be spent coding your game, marketing, playing frisbee, etc.
* Could run slowly depending on your hardware


## Step 3: Building your Game For iOS

If you're running Windows or Linux, you can still build for iOS, but instead of creating a .ipa file, Unity builds an XCode project. You can then open that project on your VM or cloud machine and continue the build process from there.

However, that's not the way I would suggest you go about it. The extra step of transferring the XCode project to your macOS machine is time consuming, and in my experience you may encounter some cryptic errors if XCode isn't configured just right.

So instead I would suggest you check out [Unity Cloud Build](https://unity3d.com/unity/features/cloud-build). It costs $9 per month, but in my opinion it's well worth it. All you have to do is point Unity to your repo on Github, or whatever hosting service you're using for your code, and Unit will automatically build for both Android and iOS every time you push a commit. This also has the added benefit of letting you continue coding your game while your project is building. When you're setting up your project's repo, I recommend creating a new branch called something like "unity-cloud-build" which just contains your "Assets" and "Project Settings" folders.

In order to publish your game on TestFlight or the App store, you're going to need to generate the appropriate certificates and provisioning profiles [here](https://developer.apple.com/account/resources/certificates). Unity's documentation has a [useful tutorial](https://docs.unity3d.com/Manual/UnityCloudBuildiOS.html) for setting these up correctly.

Once you have the appropriate p12 file and provisioning profile, you will need to add them to Unity for the build process. Go to Edit > Project Settings > Player > Other Settings > Identification. You can [download your provisioning profile](https://developer.apple.com/account/resources/profiles/), and add it here. Also make sure the [Bundle Identifier (com.CompanyName.AppName) and Signing Team ID](https://developer.apple.com/account/resources/identifiers/) are correct.

With these parameters set up correctly, you should now be able to build your project.

## Step 4: Publishing to TestFlight / the App Store
Finally, once you have your .ipa file from Unity built, you'll want to publish it to TestFlight for beta testing. I'll just cover publishing to TestFlight here, but publishing to the App Store is a similar process.

Access macOS in whatever way you decided on, and open XCode. Now you can open Application Loader by clicking XCode > Open Developer Tool > Application Loader. Apple will now ask you for all the passwords you've accumulated up to this point, so hopefully you've written them down somewhere.

## Next Steps

Now that you've submitted your build to the Apple's Beta Review process, you can expect to wait 1-2 days for your submission to be accepted. In the meantime, you may want to figure out how you're going to get beta testers for your app. I'm not a marketing expert, you I'll direct you to the [Game Dev Underground Youtube channel](https://www.youtube.com/watch?v=cIQOCQBUKk4), which I've found to be a useful resource.

Also, now that your game published on multiple platforms (assuming you already published your beta on Google Play), it can be helpful to create a landing page for your app as well, so you can direct people to one central location to download your app. It's also just nice to have a place to showcase your app that you have complete control over. [The landing page for my game](https://getjuggl.com/) is a pretty minimal example, so I would suggest you check out [some more professional examples](https://spyrestudios.com/26-landing-pages-for-video-games/) for inspiration.

As a side note, Unity is currently working on the [Unity Distribution Portal](https://unity.com/unity-distribution-portal) which allows your to publish your apps on multiple app stores at once. It doesn't currently support publishing to the App Store or Google Play, so it's not that useful at the moment. I expect Google to agree to collaborate with Unity eventually, but I have less hope for Apple, given their general business strategy of keeping everything proprietary and exclusive. The possibility that some of the more tedious aspects of cross-platform publishing could be reduced is exciting at least.

I hope you've found this tutorial helpful. Apple would probably prefer that you but their devices, which large game companies can afford to do, but is often outside of the budget of indie developers or hobbyists. If you run into any difficulties, be sure to let me know in the comments and I'll do my best to help.