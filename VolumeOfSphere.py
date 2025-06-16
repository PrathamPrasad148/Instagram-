from manim import *

class SphereVolumeFromAngle(Scene):
    def construct(self):
        # Title
        title = Text("Volume of a Sphere via Single Integration (Angle dθ)").to_edge(UP)
        self.play(Write(title))

        # Left: Semicircle (cross-section of sphere)
        radius = 2
        semicircle = Arc(radius=radius, start_angle=PI, angle=PI, color=BLUE)
        center = Dot(point=ORIGIN, color=WHITE)
        r_line = Line(ORIGIN, semicircle.point_at_angle(PI / 4), color=YELLOW)
        dtheta_arc = Arc(radius=0.5, start_angle=PI / 4 - 0.15, angle=0.3, color=GREEN)
        dtheta_label = MathTex("d\\theta").move_to(dtheta_arc.get_center() + 0.3 * RIGHT)

        # Highlight element
        wedge1 = Line(ORIGIN, semicircle.point_at_angle(PI / 4), color=ORANGE)
        wedge2 = Line(ORIGIN, semicircle.point_at_angle(PI / 4 + 0.3), color=ORANGE)
        arc_edge = Arc(radius=radius, start_angle=PI / 4, angle=0.3, color=ORANGE)
        wedge = VGroup(wedge1, wedge2, arc_edge)

        # Radius label
        r_label = MathTex("R").next_to(r_line, UP)

        # Group diagram
        diagram = VGroup(semicircle, center, r_line, r_label, wedge, dtheta_arc, dtheta_label)
        diagram.to_edge(LEFT, buff=0.5)

        self.play(Create(semicircle), FadeIn(center))
        self.play(Create(r_line), Write(r_label))
        self.play(Create(wedge))
        self.play(Create(dtheta_arc), Write(dtheta_label))
        self.wait(1)

        # Right side: Derivation steps
        derivation = VGroup(
            MathTex(r"dV = \pi y^2 \cdot R\, d\theta"),
            MathTex(r"y = R \sin\theta"),
            MathTex(r"\Rightarrow dV = \pi (R\sin\theta)^2 \cdot R\, d\theta"),
            MathTex(r"= \pi R^3 \sin^2\theta\, d\theta"),
            MathTex(r"V = \int_0^\pi \pi R^3 \sin^2\theta\, d\theta"),
            MathTex(r"= \pi R^3 \int_0^\pi \frac{1 - \cos 2\theta}{2}\, d\theta"),
            MathTex(r"= \pi R^3 \cdot \frac{\pi}{2}"),
            MathTex(r"= \frac{\pi^2 R^3}{2}"),
            MathTex(r"\text{Full Sphere: } V = \frac{4}{3} \pi R^3")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.8).to_edge(RIGHT)

        for step in derivation:
            self.play(Write(step))
            self.wait(0.5)

        self.wait(2)
