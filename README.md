# Zorang FT Project
<h3>Approach to the to find the optimal routes for delivery agents to deliver parcels from a store to consumers.</h3>
<ol>
<li>I have retrieved data from the URL in variable ‘res’ and stored the store location in variables ‘storex’, ‘storey’.</li>
<li>Latitude, Longitude, and id of delivery location have been stored in an array, namely ‘order.’</li>
<li>We have to find the minimum distance that the delivery agent has to cover to deliver the parcels from store to consumers and return to the store in minimum time.</li>
<li>Now, I have applied binary search algorithm to find the minimum of maximum distance at which the delivery agents can deliver the parcel to all consumers.</li>
<li>In the Algorithm, variable ‘mid’ refers to minimum of maximum distance covered by the delivery agent, variable ‘l’ refers to the lowest possible distance that the agent can cover and variable ‘r’ refers to the maximum possible distance that the agent can cover.</li>
<li>If condition is true then the order will be stored in array ‘temporder’ and ultimately, It’ll be copied to ‘agentdeliveries’ otherwise it’ll be checked for different value of 'mid' which has been calculated using l and r.</li>
<li>Once the loop ended, we’ll print the ‘agentdeliveries’.</li>
</ol>

The required comments are written in the python program.

<hr>
<h3>Problem Statement of development Project.</h3>
Design and create algorithm for finding the optimal routes for delivery agents to deliver parcels from a store to consumers.
<br>
<b>Requirements and constraints:</b>
<br>
● There are 100 orders which are to be delivered by 10 delivery agents.<br>
● There is one store location from where all orders will be delivered and after finishing the deliveries, the agents will come back to the store.<br>
● You are given 100 random addresses where parcels are to be delivered.<br>
● Map an optimal route for each delivery person for doing the deliveries and in what order they will do the deliveries.<br>
● It is not required that all delivery agents will deliver the same number of orders<br>
● Each delivery agent can pick multiple orders in one trip. Each agent will deliver at least one order.<br>
<b>Assumptions:</b><br>
● All 100 orders are ready at the same time<br>
● All delivery agents go at the same speed<br>
● Consider straight line distance between any two coordinates<br>
<b>Problem:</b><br>
Design optimal routes for all 10 delivery agents so that all packages are delivered and delivery agents return to the store in shortest amount of time
<b>Input</b>
Store location<br>
Latitude - 28.9428, Longitude - 77.2276<br>
Addresses to deliver- https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json <br>

<b>Output</b>
Return array of location id each agent will deliver<br>
Consider agents at index 0-9<br>
Each subarray will contain addresses id that agent will deliver and in order they deliver.<br>
[[1,2,3,9...] , [33, 45, 56], ....., [99], [100, 23]]<br>
