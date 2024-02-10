package com.ghada.loginregistration.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.ghada.loginregistration.models.Recipe;

@Repository
public interface RecipeRepository extends CrudRepository<Recipe, Long> {

	List<Recipe> findAll();

}
