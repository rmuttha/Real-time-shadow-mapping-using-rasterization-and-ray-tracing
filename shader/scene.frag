#version 330 core
out vec4 FragColor;

in vec2 TexCoords;
in vec3 FragPos;
in vec3 Normal;

uniform sampler2D shadowMap;
uniform sampler2D texture_diffuse1;
uniform vec3 lightPos;
uniform vec3 viewPos;
uniform mat4 lightSpaceMatrix;

float ShadowCalculation(vec4 fragPosLightSpace) {
    // Perform perspective divide
    vec3 projCoords = fragPosLightSpace.xyz / fragPosLightSpace.w;
    projCoords = projCoords * 0.5 + 0.5;

    // Get closest depth value from light's perspective (using [0,1] range)
    float closestDepth = texture(shadowMap, projCoords.xy).r;
    // Get depth of current fragment from light's perspective
    float currentDepth = projCoords.z;

    // Check whether current frag pos is in shadow
    float shadow = currentDepth > closestDepth + 0.005 ? 1.0 : 0.0;

    // Perform shadow bias correction here for more accurate shadows
    return shadow;
}

void main() {
    vec3 color = texture(texture_diffuse1, TexCoords).rgb;
    vec3 normal = normalize(Normal);
    vec3 lightColor = vec3(1.0);

    // Ambient
    vec3 ambient = 0.15 * lightColor;

    // Diffuse
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(lightDir, normal), 0.0);
    vec3 diffuse = diff * lightColor;

    // Shadow
    vec4 fragPosLightSpace = lightSpaceMatrix * vec4(FragPos, 1.0);
    float shadow = ShadowCalculation(fragPosLightSpace);

    // Combine results
    vec3 lighting = (ambient + (1.0 - shadow) * diffuse) * color;
    FragColor = vec4(lighting, 1.0);
}
