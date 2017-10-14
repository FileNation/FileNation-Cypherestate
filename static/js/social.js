function getCredit(){
	var title = document.getElementById("Title").innerHTML;
	var link = window.location.href;
	return [title, link]
}

function getTwitterMessage(title, link){
	var defaulted = "https://cypherestate.org";
	var loc = "https://twitter.com/intent/tweet/?text=";
	var mess= "Authorless Collaborative stories @cypherestate. Check "+title+"&amp;url="+defaulted;
	return loc+mess
} 

function getTumblrMessage(title, link){
	var defaulted = "https://cypherestate.org";
	var loc = "https://www.tumblr.com/widgets/share/tool?posttype=link&amp;title=";
	var title = title;
	var mess = "Collaborative stories 140 characters at a time.";
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
	var mess = "Collaborative stories 140 characters at a time. Check "+title+": "+link;
	return loc+mess
}

function getYnewsMessage(title, link){
	var loc = "https://news.ycombinator.com/submitlink?u="
	var args = "&amp;t=Collaborative stories 140 characters at a time."
	return loc+link+args
}

function getMailMessage(title, link){
	var mess = "mailto:?subject=Cypherestate: "+title+"&amp;body=Hey! Check this out: "+link;
	return mess
}

var credit = getCredit();
var title = credit[0];
var link = credit[1];

// link = "https://ericalcaide.com";
// title = "Hello, it's me";

// console.log(getTwitterMessage(title, link));
// console.log(getTumblrMessage(title, link));
// console.log(getRedditMessage(title, link));
// console.log(getWhatsappMessage(title, link));
// console.log(getYnewsMessage(title, link));
// console.log(getMailMessage(title, link));

