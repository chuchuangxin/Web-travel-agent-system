
/* --- 全景信息描述 --------------------------------------- 
显示在网页标题和全景信息窗里的描述信息，可自行设计内容和样式，和普通网页一样。
*/

vrTitle = 'RMPANO JS v1.0.1'; 
vrDescription = "RMPANO HTML5版本正式发布！支持safari和chrome浏览器，支持iPhone、iPad、iPod设备。支持立方体的六张图和条形图，支持预览，支持自定义控制面板，支持背景音乐。<br><img src='img/control/icon.png'>"; 

/*
全景图地址，预览图使用横向或纵向条形图，全景图支持两种模式：立方体6张图，立方体条形图；
*/
preview = "static/img/cube/2/preview.jpg";
/*6张图*/
panoType = "cube";
cube_f = "static/img/cube/2/f.jpg";
cube_r = "static/img/cube/2/r.jpg";
cube_b = "static/img/cube/2/b.jpg";
cube_l = "static/img/cube/2/l.jpg";
cube_u = "static/img/cube/2/u.jpg";
cube_d = "static/img/cube/2/d.jpg";
/*条形图*/
//panoType = "cubestrip";
//cubestrip = "pano0.jpg";

/* --- 初始化设置：atartPan:初始横向角度，startTilt：初始纵向角度，startFov:初始视角 ------------------------------------ */
startPan = 40; 			/* 从左到右：-180 - 0 - 180 */
startTilt = 10; 			/* 从下到上：-90 - 0 - 90 */
startFov = 70; 			/* 视角：30 - 130 */
fovMax = 120;			/*最大视角*/
fovMin = 30;			/*最小视角*/

/* --- 视角限制 ------------------------------ */
useLimits = false;
topLimit = 60;  		/* 0 - 90 */
bottomLimit = -60;		/* 0 - -90 */
leftLimit = -120; 		/* 0 - -180 */
rightLimit = 120; 		/* 0 - 180*/

/* --- 控制面板 ----------------------------------*/

useControl = "static/img/control/button.png";
autoRotateOnStart = true; 
autoRotateOnIdle = true; 
autoRotateDelay = 5; /* 秒 */ 


	
/* --- 背景声音 ----------------------------- 
背景声音,同audio标签属性 */

//bgSound = "src='sound.mp3' autobuffer autoplay loop";

