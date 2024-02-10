package com.ghada.loginregistration.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ghada.loginregistration.models.Recipe;
import com.ghada.loginregistration.repositories.RecipeRepository;

@Service
public class RecipeService {
	
	@Autowired
	private RecipeRepository recipeRepo;
	
	public List<Recipe> allRecipes(){
		return recipeRepo.findAll();
	}
	
	public Recipe findOne(Long id) {
		Optional<Recipe> opRecipe = recipeRepo.findById(id);
		
		if(opRecipe.isPresent()) {
			return opRecipe.get();
			
		}else {
			return null;
		}
	}
	
	public Recipe create(Recipe recipe) {
		return recipeRepo.save(recipe);
	}
	
	public Recipe update(Recipe recipe) {
		return recipeRepo.save(recipe);
	}
	
	public void delete (Long id) {
		recipeRepo.deleteById(id);
	}
}
