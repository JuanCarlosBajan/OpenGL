vertex_shader ='''
#version 450 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;
uniform float random;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;

    if(random >=0.5) {
        pos = (modelMatrix * vec4(position+(abs(sin(time))*norms/5), 1.0)).xyz;
        gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position+(abs(sin(time))*norms/5), 1.0);
    } else {
        pos = (modelMatrix * vec4(position, 1.0)).xyz;
        gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
    }
}
'''

fragment_shader ='''
#version 450 core
out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(tex, UVs) * intensity;
}
'''

toon_shader ='''
#version 450 core
out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));


    if(intensity > 0.9) {       
        fragColor = texture(tex, UVs) * 1;
    }
    else if(intensity > 0.8) {       
        fragColor = texture(tex, UVs) * 0.8;
    }
    else if(intensity > 0.6) {       
        fragColor = texture(tex, UVs) * 0.6;
    }
    else if(intensity > 0.4) {       
        fragColor = texture(tex, UVs) * 0.4;
    }
    else if(intensity > 0.2) {       
        fragColor = texture(tex, UVs) * 0.2;
    }

}
'''