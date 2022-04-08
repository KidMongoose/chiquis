% rebase('en/base.tpl') 
% include('en/header.tpl')
<div id="documentation">
   <div id="documentation-header"><h1>Documentation</h1></div>
   <article>
     <h2>Get newest photo</h2>
     <div class="api-flex">
       <code>https://chiquis.pet/api/en/newest/?photo=1</code>
       <a href="#" class="copy">copy</a>
      </div>   
       <p>Get the newest photo of Chiquis</p>
       <h2>Response</h2>
       <div class="api-flex"><code></code></div>
   </article>
    <article>
      <h2>Get random photo</h2>
    <div class="api-flex">
        <code>https://chiquis.pet/api/en/photo/random/</code>
        <a href="#" class="copy">copy</a>
      </div>   
      <p>Get a random photo of Chiquis</p>
      <h2>Response</h2>
     <div class="api-flex"><code>{"data": "/static/images/upload/IMG_5976.jpeg"}</code></div>
   </article>

   <article>
     <h2>Get oldest photo</h2>
    <div class="api-flex">
       <code>https://chiquis.pet/api/en/oldest/?photo=1</code>
       <a href="#" class="copy">copy</a>
      </div> 
       <p>Get the oldest photo of Chiquis</p>
       <h2>Response</h2>
     <div class="api-flex"><code></code></div> 
   </article>

   <article>
     <h2>Get newest video</h2>
    <div class="api-flex">
     <code>https://chiquis.pet/api/en/newest/?video=1</code>
        <a href="#" class="copy">copy</a>
      </div> 
     <p>Get the newest upload video of Chiquis</p>
     <h2>Response</h2>
     <div class="api-flex"><code></code></div>
   </article>
    <article>
      <h2>Get random video</h2>
      <div class="api-flex">
        <code>https://chiquis.pet/api/en/video/random/</code>
        <a href="#" class="copy">copy</a>
      </div> 
      <p>Get a random video of Chiquis</p>
     <h2>Response</h2>
     <div class="api-flex"><code>{"data": "/static/images/uploads/videos/IMG_6067.mov"}</code></div>
   </article>

   <article>
     <h2>Get all photo in ascending order</h2>
    <div class="api-flex">
        <code>https://chiquis.pet/api/en/photos/newest/</code>
        <a href="#" class="copy">copy</a>
      </div>
     <p>Get all of Chiquis photos in ascending order (newest to oldest)</p>
    <h2>Response</h2>
    <div class="api-flex"> <code></code> </div>
   </article>
    <article>
      <h2>Get all photos in descending order</h2>
       <div class="api-flex">
         <code>https://chiquis.pet/api/en/photos/oldest/</code>
          <a href="#" class="copy">copy</a>
      </div> 
      <p>Get all of Chiquis photos in descending order (oldest to newest)</p>
     <h2>Response</h2>
     <div class="api-flex"><code></code></div>
   </article>

   <article>
     <h2>Get all videos in ascending order</h2>
    <div class="api-flex">
        <code>https://chiquis.pet/api/en/videos/newest/</code>
        <a href="#" class="copy">copy</a>
      </div>
     <p>Get all of Chiquis videos in ascending order (newest to oldest)</p>
    <h2>Response</h2>
     <div class="api-flex"><code></code></div>
   </article>
    <article>
      <h2>Get all videos in descending order</h2>
       <div class="api-flex">
         <code>https://chiquis.pet/api/en/videos/oldest/</code>
          <a href="#" class="copy">copy</a>
      </div> 
      <p>Get all of Chiquis videos in descending order (oldest to newest)</p>
      <h2>Response</h2>
     <div class="api-flex"><code></code></div>
   </article>
</div>
% include('en/footer.tpl')