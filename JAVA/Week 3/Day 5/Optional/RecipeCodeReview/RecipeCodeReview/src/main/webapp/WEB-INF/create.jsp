<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<!-- c:out ; c:forEach etc. --> 

<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!-- Formatting (dates) --> 

<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"  %>

<!-- form:form -->

<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<!-- for rendering errors on PUT routes -->

<%@ page isErrorPage="true" %>

<!DOCTYPE html>

<html>

<head>

    <meta charset="UTF-8">

    <title>Title</title>

    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css">

    <link rel="stylesheet" href="/css/main.css"> <!-- change to match your file/naming structure -->

    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>

    <script type="text/javascript" src="/js/app.js"></script><!-- change to match your file/naming structure -->

</head>

<body>

	<div class="container">

   		<div class="navbar navbar-expand-lg navbar-light bg-light">

               <h1 class="navbar-brand">Hello ${user.userName }</h1>



               <div class="collapse navbar-collapse d-flex justify-content-between">

                   <ul class="navbar-nav mr-auto">

                       <li>

                           <a href="/welcome" class="btn btn-outline-success">Dashboard</a>

                       </li>

                   </ul>

                   <form action="/logout" method="post" class="form-inline my-2 my-lg-0">

                    <button class="btn btn-danger my-2 my-sm-0">logout</button>

                </form>



            </div>

        </div>



        <form:form action="/recipe/new" method="post" modelAttribute="newRecipe">



            <p>

                <form:label path="name">Name</form:label>

                <form:errors path="name" class="text-danger"/>

                <form:input class="form-control" path="name"/>

            </p>

            <p>

                <form:label path="path">Image</form:label>

                <form:errors path="path" class="text-danger"/>

                <form:input class="form-control" path="path"/>

            </p>



            <p>

                <form:label path="description">Description</form:label>

                <form:errors path="description" class="text-danger"/>

                <form:textarea class="form-control" path="description"/>

            </p>





            <br />

            <input type="submit" value="Submit" class="btn btn-success"/>

        </form:form>

 	</div>

</body>

</html>