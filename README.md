Scrapy Tutorial
https://www.youtube.com/watch?v=mBoX_JCKZTE&t=1218s

CSS
https://www.youtube.com/watch?v=hkDAW7hhEYU

CSS simply speaking
 tag name has no pre/suffix
 class name add a "." in front of it. Eg <li class="product"> => css(li.product)
 id add "#"
 if tag inside tag then css(h a::whatever)
"::" => the attriubte inside, ie text, or attr(href)
css('h3 a::attr(href)')
in scrapy if add .get() then will get the attribute of the first response. If only response.css(xxx) will return all the tags with that css elements
