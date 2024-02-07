package com.hellohuman.greeting;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Greet {
	@GetMapping("")
		public String index(@RequestParam(value="name" , required  = false)String name ,
					@RequestParam(value="last_name" , required  = false)String last_name ,
					@RequestParam(value="times" , required  = false)int times )  {
		if(name == null ) {
			return "Hello Human";
		} else {
			String result = "Hello " + name + " " + last_name;

			for(int i = 1; i < times ; i++) {
				result+= " Hello " + name + " " + last_name;
			}
			return result;
		}
	}
}

