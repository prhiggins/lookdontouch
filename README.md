# lookdontouch
A naughty (the fun kind) and mostly harmless experiment involving URL previews.

## Abstract
Messaging services, including Facebook Messenger, Twitter, and iMessage query URLs without being prompted by the user. If the application generates the URL preview from the user's device, the recipient simply viewing the message containing the link is sufficient to initiate a request to the server. This enables the 0-click collection of user and device data, including IP address and HTTP headers. This project explores various applications of this feature.

## Applications
The automatic loading of URL previews can provide information useful to many perspectives. While collecting (admittedly fairly minimal) HTTP request data from a target is an obvious application, perhaps even more useful is the ability to monitor the transmission of a given link. For example, a good-faith user could determine calls that are being made to assemble URL previews, either by the resources requested, or by the origin of the request. While some preview-generating services make HTTP requests through the end user's device, other applications, notably news feeds, may rely on a centralized bot to compile previews. Tracking hits on URL previews can provide insight on if and how a link is being shared across the web. Using this data, it may even be possible to approximate the frequency and quantity of that traffic.

This repository explores potentially unintended and/or exploitative uses of this feature, mainly with the benefit of the server operator in mind.
