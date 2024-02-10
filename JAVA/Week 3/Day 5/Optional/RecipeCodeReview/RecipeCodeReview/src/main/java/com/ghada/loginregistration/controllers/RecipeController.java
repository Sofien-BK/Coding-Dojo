package com.ghada.loginregistration.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.ghada.loginregistration.models.Recipe;
import com.ghada.loginregistration.models.User;
import com.ghada.loginregistration.services.RecipeService;
import com.ghada.loginregistration.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@Controller
public class RecipeController {

	@Autowired
	private RecipeService recipeServ;
	
	@Autowired
	private UserService userServ;
	
	
	// ====Display Route==== Home page
		@GetMapping("/recipes")
		public String dashboard(HttpSession session, Model model) {
			Long id = (Long) session.getAttribute("userID");
			if (id == null) {
				//if the user is not logged in we should redirect him to the landing page
				return "redirect:/";
			} else {
				//get the logged in user
				User loggedinUser = userServ.findOne(id);
				model.addAttribute("user", loggedinUser);
				
				List<Recipe> allRecipes = recipeServ.allRecipes();
				
				model.addAttribute("allRecipes", allRecipes);
				return "dashboard.jsp";
			}
		}

		@GetMapping("/recipes/new")
		public String create(@ModelAttribute("newRecipe") Recipe newRecipe,BindingResult result,HttpSession session, Model model) {
			Long id = (Long) session.getAttribute("userID");
			if (id == null) {
				//if the user is not logged in we should redirect him to the landing page
				return "redirect:/";
			} else {
				//get the logged in user
				User loggedinUser = userServ.findOne(id);
				model.addAttribute("user", loggedinUser);
			return"create.jsp";
		}
		}
		
		@PostMapping("/recipe/new")
		public  String newRecipe(@Valid @ModelAttribute ("newRecipe") Recipe newRecipe,BindingResult result) {
			if(result.hasErrors()) {
				return "create.jsp";
			}else {
				recipeServ.create(newRecipe);
				return "redirect:/recipes"; 
			}
		}
}
