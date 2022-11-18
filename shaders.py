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

    
    pos = (modelMatrix * vec4(position, 1.0)).xyz;
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
    
}
'''

x_shader ='''
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

    
    if(sin(position.y*100) > 0.5) {
        pos = (modelMatrix * vec4(position+norms*0.07, 1.0)).xyz;
        gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position+norms*0.07, 1.0);
    }
    else {
        pos = (modelMatrix * vec4(position, 1.0)).xyz;
        gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
    }
    
}
'''

big_shader ='''
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

        pos = (modelMatrix * vec4(position+norms*0.07, 1.0)).xyz;
        gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position+norms*0.07, 1.0);
    
}
'''

small_shader ='''
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

        pos = (modelMatrix * vec4(position-norms*0.07, 1.0)).xyz;
        gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position-norms*0.07, 1.0);
    
}
'''

hulk_shader ='''
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
    fragColor = texture(tex, UVs) * (intensity+0.2);
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
        fragColor = texture(tex, UVs) * 1.0;
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
    else{
        fragColor = vec4(0,0,0,0);
    }

}
'''

reflection_shader ='''
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


    fragColor = vec4(vec3(0,0,1*norms.x*norms.y*intensity*5),1.0);


}
'''

duende_shader ='''
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


    fragColor = vec4(vec3(0,sin(1*intensity*UVs.x*norms.x*100),0),1.0);


}
'''

tiktok_shader ='''
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


    fragColor = vec4(vec3(cos(1*intensity*UVs.x*norms.x*100),sin(1*intensity*UVs.x*norms.x*100),sin(1*intensity*UVs.x*norms.x*100)),1.0);


}
'''

nothing_shader ='''
#version 450 core
out vec4 fragColor;

uniform float randomr;
uniform float randomg;
uniform float randomb;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    
    fragColor = vec4(sin(randomr*100)*norms.x,cos(randomg*100)*norms.y,sin(randomb*100)*norms.z,1.0);

}
'''