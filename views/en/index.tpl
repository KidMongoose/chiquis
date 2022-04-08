% rebase('en/base.tpl') 
% include('en/header.tpl')
<main>
  <div id="content">
  <div id="content-header"><h1>New photos & videos</h1></div>
 % for post, video in posts:
   <div class="content-item">
     <h2>{{post['title']}}</h2>
     <p>{{post['date']}}</p>
     % if post['image']:
         <img src="static/images/uploads/{{post['image']}}" alt="">
     % end  
   </div>   
    <div class="content-item">
     % if video['video']:
        <h2>{{video['title']}}</h2>  
        <p>{{video['date']}}</p>
         <video controls>
           <source src="static/images/uploads/videos/{{video['video']}}" type="video/mp4">
         </video>
     % end
     </div>
 % end
</div>
</main>
% include('en/footer.tpl')
