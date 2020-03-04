uniform float theta;
attribute float distance;
attribute vec4 color;
attribute vec2 position;
varying vec4 v_color;

void main() {
    float ct = cos(theta);
    float st = sin(theta);
    float x = 0.75 * (position.x * ct - position.y * st);
    float y = 0.75 * (position.x * st + position.y * ct);
    gl_Position = vec4(x, y, 0.0, distance);
    v_color = color;
}
