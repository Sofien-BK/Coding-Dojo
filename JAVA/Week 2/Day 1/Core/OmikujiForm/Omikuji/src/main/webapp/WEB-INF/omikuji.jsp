<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <!-- New line below to use the JSP Standard Tag Library -->
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Demo JSP</title>
    </head>
<body>
    <h1>Here's your Omikuji!</h1>
	
	<h3>In ${num} years , you will live in ${city} with ${per} as your roommate,${hobby} for a living. The next time you see a ${liv} you will have a good luck. Also , ${nice}</h3>
	
	
	<a href="/omikuji">Go Back</a>
</body>
</html>
