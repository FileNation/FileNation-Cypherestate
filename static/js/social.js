function getTwitterMessage(title, link){
  var defaulted = link;
  var loc = "https://twitter.com/intent/tweet/?text=";
  var mess= "Censorless blogging on the Distributed Web @cypherestate. Check: ''"+title+"'' at &amp;url="+defaulted;
  return loc+mess
} 

function getTumblrMessage(title, link){
  var defaulted = link;
  var loc = "https://www.tumblr.com/widgets/share/tool?posttype=link&amp;title=";
  var title = title;
  var mess = "Censorless blogging on the Distributed Web";
  var args = "&amp;caption="+mess+" Check "+title+"&amp;content="+link+"&amp;canonicalUrl="+link;
  var last = "&amp;shareSource=tumblr_share_button";

  return loc+title+args+last
}

function getRedditMessage(title, link){
  var mess = "https://reddit.com/submit/?url="+link;
  return mess
}

function getWhatsappMessage(title,link){
  var loc = "whatsapp://send?text="
  var mess = "Censorless blogging on the Distributed Web. Check "+title+": "+link;
  return loc+mess
}

function getYnewsMessage(title, link){
  var loc = "https://news.ycombinator.com/submitlink?u="
  var args = "&amp;t=Censorless blogging on the Distributed Web."
  return loc+link+args
}

function getMailMessage(title, link){
  var mess = "mailto:?subject=Cypherestate: "+title+"&amp;body=Hey! Check this out: "+link;
  return mess
}