<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!-- c:out ; c:forEach etc. -->
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!-- Formatting (dates) -->
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<!-- form:form -->
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!-- for rendering errors on PUT routes -->
<%@ page isErrorPage="true"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Title</title>
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="/css/main.css">
<!-- change to match your file/naming structure -->
<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
<script type="text/javascript" src="/js/app.js"></script>
<!-- change to match your file/naming structure -->
</head>
<body>
	<div class="container">
		<div class="navbar navbar-expand-lg navbar-light bg-light">
   			<h1 class="navbar-brand">Welcome ${user.userName}</h1>
   		
   			<div class="collapse navbar-collapse d-flex justify-content-between">
   				<ul class="navbar-nav mr-auto">
   					<li>
   						<a href="/recipes/new" class="btn btn-outline-success">New Recipe!</a>
   					</li>
   				</ul>
   				<form action="/logout" method="post" class="form-inline my-2 my-lg-0">
					<button class="btn btn-danger my-2 my-sm-0">logout</button>
				</form>
		
			</div>
		</div>
		
		<c:forEach var="oneRecipe" items="${allRecipes }">
                    <div class="d-flex">
                        <img alt="${oneRecipe.name }" src="${oneRecipe.path }" class="m-5">
                        <div class="mt-5">
                            <h3> <a href="/recipe/${oneRecipe.id }" > ${oneRecipe.name } </a></h3>
                            <p>${oneRecipe.description }</p>
                        </div>
                    </div>
                    <hr>
        </c:forEach>
	</div>
</body>
</html>