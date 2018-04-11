// Include standard headers
#include <stdio.h>
#include <stdlib.h>

// Include GLEW
#include <GL/glew.h>

// Include GLFW
#include <GLFW/glfw3.h>
GLFWwindow* window;

// Include GLM
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
using namespace glm;

#include <common/shader.hpp>
#include <common/texture.hpp>
#include <common/controls.hpp>

int main( void )
{
	// Initialise GLFW
	if( !glfwInit() )
	{
		fprintf( stderr, "Failed to initialize GLFW\n" );
		getchar();
		return -1;
	}

	glfwWindowHint(GLFW_SAMPLES, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	// Open a window and create its OpenGL context
	window = glfwCreateWindow( 1024, 768, "Tutorial 0 - Keyboard and Mouse", NULL, NULL);
	if( window == NULL ){
		fprintf( stderr, "Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 version of the tutorials.\n" );
		getchar();
		glfwTerminate();
		return -1;
	}
    glfwMakeContextCurrent(window);

	// Initialize GLEW
	glewExperimental = true; // Needed for core profile
	if (glewInit() != GLEW_OK) {
		fprintf(stderr, "Failed to initialize GLEW\n");
		getchar();
		glfwTerminate();
		return -1;
	}

	// Ensure we can capture the escape key being pressed below
	glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);
    // Hide the mouse and enable unlimited mouvement
    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
    
    // Set the mouse at the center of the screen
    glfwPollEvents();
    glfwSetCursorPos(window, 1024/2, 768/2);

	// Dark blue background
	glClearColor(0.0f, 0.0f, 0.4f, 0.0f);

	// Enable depth test
	glEnable(GL_DEPTH_TEST);
	// Accept fragment if it closer to the camera than the former one
	glDepthFunc(GL_LESS); 

	// Cull triangles which normal is not towards the camera
	// glEnable(GL_CULL_FACE);

	GLuint VertexArrayID;
	glGenVertexArrays(1, &VertexArrayID);
	glBindVertexArray(VertexArrayID);

	// Create and compile our GLSL program from the shaders
	GLuint programID = LoadShaders( "TransformVertexShader.vertexshader", "TextureFragmentShader.fragmentshader" );
	// GLuint programID = LoadShaders( "TransformVertexShader.vertexshader", "SimpleFragmentShader.fragmentshader" );

	// Get a handle for our "MVP" uniform
	GLuint MatrixID = glGetUniformLocation(programID, "MVP");

	// Load the texture
	GLuint Texture = loadDDS("uvtemplate.DDS");
	
	// Get a handle for our "myTextureSampler" uniform
	GLuint TextureID  = glGetUniformLocation(programID, "myTextureSampler");

	// Our vertices. Tree consecutive floats give a 3D vertex; Three consecutive vertices give a triangle.
	// A cube has 6 faces with 2 triangles each, so this makes 6*2=12 triangles, and 12*3 vertices
	static const GLfloat g_vertex_buffer_data[] = { 
		// left body				
		0.2f, 0.6f, 0.0f,	//0
		0.2f, 0.6f, -0.6f, 	//1
		0.3f, 0.4f, -0.7f,	//2

		0.3f, 0.0f, -0.7f,	//3 
		0.3f, 0.0f, 0.4f,	//4
		0.3f, 0.3f, 0.4f,	//5

		0.3f, 0.4f, 0.2f,	//6

		//right body		
		-0.2f, 0.6f, 0.0f,
		-0.2f, 0.6f, -0.6f,
		-0.3f, 0.4f, -0.7f,

		-0.3f, 0.0f, -0.7f,
		-0.3f, 0.0f, 0.4f,
		-0.3f, 0.3f, 0.4f,
		
		-0.3f, 0.4f, 0.2f,

		//wheel 1
		0.3f, 0.0f, 0.1f, 	// center (14)
		0.3f, 0.08f, 0.15f,
		0.3f, 0.08f, 0.05f,
		0.3f, 0.0f, 0.0f,
		0.3f, -0.08f, 0.05f,
		0.3f, -0.08f, 0.15f,
		0.3f, 0.0f, 0.2f,

		// 0.28f, 0.0f, 0.1f, 	// center (21)
		// 0.28f, 0.08f, 0.15f,
		// 0.28f, 0.08f, 0.05f,
		// 0.28f, 0.0f, 0.0f,
		// 0.28f, -0.08f, 0.05f,
		// 0.28f, -0.08f, 0.15f,
		// 0.28f, 0.0f, 0.2f,

		//wheel 2 (-0.4 -0.1 -0.5)
		0.3f, 0.0f, -0.45f, 	// center (28)
		0.3f, 0.08f, -0.4f,
		0.3f, 0.08f, -0.5f,
		0.3f, 0.0f, -0.55f,
		0.3f, -0.08f, -0.5f,
		0.3f, -0.08f, -0.4f,
		0.3f, 0.0f, -0.35f,

		// 0.28f, 0.0f, -0.45f, 	// center (35)
		// 0.28f, 0.08f, -0.4f,
		// 0.28f, 0.08f, -0.5f,
		// 0.28f, 0.0f, -0.55f,
		// 0.28f, -0.08f, -0.5f,
		// 0.28f, -0.08f, -0.4f,
		// 0.28f, 0.0f, -0.35f,

		//wheel 3
		-0.3f, 0.0f, 0.1f, 	// center (42)
		-0.3f, 0.08f, 0.15f,
		-0.3f, 0.08f, 0.05f,
		-0.3f, 0.0f, 0.0f,
		-0.3f, -0.08f, 0.05f,
		-0.3f, -0.08f, 0.15f,
		-0.3f, 0.0f, 0.2f,

		// -0.28f, 0.0f, 0.1f, 	// center (49)
		// -0.28f, 0.08f, 0.15f,
		// -0.28f, 0.08f, 0.05f,
		// -0.28f, 0.0f, 0.0f,
		// -0.28f, -0.08f, 0.05f,
		// -0.28f, -0.08f, 0.15f,
		// -0.28f, 0.0f, 0.2f,

		//wheel 2 (-0.4 -0.1 -0.5)
		-0.3f, 0.0f, -0.45f, 	// center (56)
		-0.3f, 0.08f, -0.4f,
		-0.3f, 0.08f, -0.5f,
		-0.3f, 0.0f, -0.55f,
		-0.3f, -0.08f, -0.5f,
		-0.3f, -0.08f, -0.4f,
		-0.3f, 0.0f, -0.35f,

		// -0.28f, 0.0f, -0.45f, 	// center (63)
		// -0.28f, 0.08f, -0.4f,
		// -0.28f, 0.08f, -0.5f,
		// -0.28f, 0.0f, -0.55f,
		// -0.28f, -0.08f, -0.5f,
		// -0.28f, -0.08f, -0.4f,
		// -0.28f, 0.0f, -0.35f,

	};

	GLuint vertexbuffer;
	glGenBuffers(1, &vertexbuffer);
	glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
	glBufferData(GL_ARRAY_BUFFER, sizeof(g_vertex_buffer_data), g_vertex_buffer_data, GL_STATIC_DRAW);

	static const GLushort indices[] = {
		0, 1, 2,
		0, 2, 6,
		2, 3, 6,
		3, 4, 6,
		4, 5, 6,
				
		7, 8, 9,
		7, 9, 13,
		9, 10, 13,
		10, 11, 13,
		11, 12, 13,

		4, 11, 12,
		4, 12, 5,

		5, 12, 13,
		5, 13, 6,

		6, 13, 7,
		6, 7, 0,

		0, 7, 8,
		0, 8, 1,

		1, 8, 9,
		1, 9, 2,

		2, 9, 10,
		2, 10, 3,

		3, 10, 11,
		3, 11, 4,

		// wheel1
		14, 15, 16,
		14, 16, 17,
		14, 17, 18,
		14, 18, 19,
		14, 19, 20,
		14, 20, 15,

		// wheel2
		21, 22, 23,
		21, 23, 24,
		21, 24, 25,
		21, 25, 26,
		21, 26, 27,
		21, 27, 22,

		// wheel3
		21+7, 22+7, 23+7,
		21+7, 23+7, 24+7,
		21+7, 24+7, 25+7,
		21+7, 25+7, 26+7,
		21+7, 26+7, 27+7,
		21+7, 27+7, 22+7,

		// wheel
		21+14, 22+14, 23+14,
		21+14, 23+14, 24+14,
		21+14, 24+14, 25+14,
		21+14, 25+14, 26+14,
		21+14, 26+14, 27+14,
		21+14, 27+14, 22+14,

		// 15, 22, 23,
		// 15, 23, 16,
		// 16, 23, 24,
		// 16, 24, 17,
		// 17, 24, 25,
		// 17, 25, 18,
		// 18, 25, 26,
		// 18, 26, 19,
		// 19, 26, 27,
		// 19, 27, 20,
		// 20, 27, 22,
	};

	GLuint indexbuffer;
	glGenBuffers(1, &indexbuffer);
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexbuffer);
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

	// Two UV coordinatesfor each vertex. They were created with Blender.
	static const GLfloat g_uv_buffer_data[] = { 
		0.000059f, 0.000004f, 
		0.000103f, 0.336048f, 
		0.335973f, 0.335903f, 
		1.000023f, 0.000013f, 
		0.667979f, 0.335851f, 
		0.999958f, 0.336064f, 
		0.667979f, 0.335851f, 
		0.336024f, 0.671877f, 
		0.667969f, 0.671889f, 
		1.000023f, 0.000013f, 
		0.668104f, 0.000013f, 
		0.667979f, 0.335851f, 
		0.000059f, 0.000004f, 
		0.335973f, 0.335903f, 
		0.336098f, 0.000071f, 
		0.667979f, 0.335851f, 
		0.335973f, 0.335903f, 
		0.336024f, 0.671877f, 
		1.000004f, 0.671847f, 
		0.999958f, 0.336064f, 
		0.667979f, 0.335851f, 
		0.668104f, 0.000013f, 
		0.335973f, 0.335903f, 
		0.667979f, 0.335851f, 
		0.335973f, 0.335903f, 
		0.668104f, 0.000013f, 
		0.336098f, 0.000071f, 
		0.000103f, 0.336048f, 
		0.000004f, 0.671870f, 
		0.336024f, 0.671877f, 
		0.000103f, 0.336048f, 
		0.336024f, 0.671877f, 
		0.335973f, 0.335903f, 
		0.667969f, 0.671889f, 
		1.000004f, 0.671847f, 
		0.667979f, 0.335851f
	};

	GLuint uvbuffer;
	glGenBuffers(1, &uvbuffer);
	glBindBuffer(GL_ARRAY_BUFFER, uvbuffer);
	glBufferData(GL_ARRAY_BUFFER, sizeof(g_uv_buffer_data), g_uv_buffer_data, GL_STATIC_DRAW);

	do{

		// Clear the screen
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		// Use our shader
		glUseProgram(programID);

		// Compute the MVP matrix from keyboard and mouse input
		computeMatricesFromInputs();
		glm::mat4 ProjectionMatrix = getProjectionMatrix();
		glm::mat4 ViewMatrix = getViewMatrix();
		glm::mat4 ModelMatrix = glm::mat4(1.0);
		glm::mat4 MVP = ProjectionMatrix * ViewMatrix * ModelMatrix;

		// Send our transformation to the currently bound shader, 
		// in the "MVP" uniform
		glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &MVP[0][0]);

		// Bind our texture in Texture Unit 0
		glActiveTexture(GL_TEXTURE0);
		glBindTexture(GL_TEXTURE_2D, Texture);
		// Set our "myTextureSampler" sampler to use Texture Unit 0
		glUniform1i(TextureID, 0);

		// 1rst attribute buffer : vertices
		glEnableVertexAttribArray(0);
		glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
		glVertexAttribPointer(
			0,                  // attribute. No particular reason for 0, but must match the layout in the shader.
			3,                  // size
			GL_FLOAT,           // type
			GL_FALSE,           // normalized?
			0,                  // stride
			(void*)0            // array buffer offset
		);

		// Draw the triangle !
		// glDrawArrays(GL_TRIANGLES, 0, 12*3); // 12*3 indices starting at 0 -> 12 triangles
		glDrawElements(GL_TRIANGLES, sizeof(indices)/sizeof(indices[0]), GL_UNSIGNED_SHORT, NULL);

		glDisableVertexAttribArray(0);
		glDisableVertexAttribArray(1);

		// Swap buffers
		glfwSwapBuffers(window);
		glfwPollEvents();

	} // Check if the ESC key was pressed or the window was closed
	while( glfwGetKey(window, GLFW_KEY_ESCAPE ) != GLFW_PRESS &&
		   glfwWindowShouldClose(window) == 0 );

	// Cleanup VBO and shader
	glDeleteBuffers(1, &vertexbuffer);
	glDeleteBuffers(1, &uvbuffer);
	glDeleteProgram(programID);
	glDeleteTextures(1, &TextureID);
	glDeleteVertexArrays(1, &VertexArrayID);

	// Close OpenGL window and terminate GLFW
	glfwTerminate();

	return 0;
}

