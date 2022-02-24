import math
from manim import *
import taylor


class SinAndCosFunctionPlot(Scene):
    def construct(self):
        self.wait()
        self.introduce_question()
        self.introduce_plot()
        self.animate_function_change()
        self.wait()

    def get_axes_plot(self) -> VGroup:
        axes = Axes(
            x_range=[-6, 6, math.pi / 2],
            y_range=[-2, 2, 1],
            y_length=self.camera.frame_width / 3,
            x_length=self.camera.frame_width,
            axis_config={"color": GREEN},
            tips=False,
        )
        axis_labels = axes.get_axis_labels()
        axis_labels.add(MathTex("\\pi").next_to(axes.coords_to_point(math.pi, 0), DOWN))
        axis_labels.add(MathTex("-\\pi").next_to(axes.coords_to_point(-math.pi, 0), DOWN))
        axis_labels.add(MathTex("1").next_to(axes.coords_to_point(0, 1), LEFT))
        return VGroup(axes, axis_labels)

    def get_plot(self, axes: Axes, func):
        return axes.plot(func, color=BLUE, x_range=[-26, 26])

    def introduce_plot(self):
        self.plot = self.get_axes_plot()
        self.play(Create(self.plot, run_time=3, lag_ratio=0.1))
        self.sin = self.plot[0].plot(lambda x: (math.sin(2 * x) ** 2), color=YELLOW)
        self.play(Create(self.sin))

    def introduce_question(self):
        self.equation = MathTex("\\sin^2(2x)")
        self.hint = Tex("Function to approximate:").move_to(2 * UP)
        self.play(FadeIn(self.hint))
        self.play(FadeIn(self.equation))
        self.play(Circumscribe(self.equation))
        self.wait(2)
        self.play(Transform(self.hint, Tex("Let's try to get rid of an exponent by using cos(x)").move_to(2 * DOWN)))
        self.wait(2)
        self.play(FadeOut(self.hint), Transform(self.equation, MathTex("\\sin^2(2x)").to_corner(UR)))
        self.wait(2)

    def animate_function_change(self):
        self.cos = self.get_plot(self.plot[0], lambda x: np.cos(x))
        titles = list(map(lambda x: MathTex(x).to_corner(corner=UP + LEFT), [
            "cos(x)", "cos(4x)", "-cos(4x)", "1-cos(4x)", "\\frac{1-cos(4x)}{2}"
        ]))
        self.play(FadeIn(titles[0]), FadeIn(self.cos))
        self.play(Circumscribe(titles[0]))
        self.wait(2)
        self.play(FadeIn(self.hint), Transform(self.hint, Tex("Let's use simple modifications ...").move_to(3 * DOWN)))
        self.play(Circumscribe(titles[0]))
        self.wait()
        self.play(FadeOut(self.hint), Transform(titles[0], titles[1]),
                  self.cos.animate.scale(np.array((.25, 1.0, 0.0))))
        self.wait()
        self.play(Transform(titles[0], titles[2]), self.cos.animate.scale(np.array((1.0, -1.0, 0.0))))
        self.wait()
        self.play(Transform(titles[0], titles[3]),
                  self.cos.animate.shift(np.array((0.0, self.plot[0].coords_to_point(0, 1)[1], 0.0))))
        self.wait()
        self.play(Transform(titles[0], titles[4]), self.cos.animate.scale(np.array((1.0, .5, 0.0)), about_edge=DOWN))
        self.wait()
        self.play(FadeOut(self.plot), FadeOut(self.cos), FadeOut(self.sin), FadeOut(self.equation))
        self.wait()
        self.play(FadeIn(self.hint),
                  Transform(self.hint, Tex("Let's apply taylor series for cos(x)").move_to(3 * DOWN)))
        equations = [
            "cos(x)=\\sum_{k=0}^{\\infty}{\\frac{(-1)^k}{(2k!)}{x}^{2k}}",
            "cos(4x)=\\sum_{k=0}^{\\infty}{\\frac{(-1)^k}{(2k!)}{(4x)}^{2k}}",
            "cos(4x)=\\sum_{k=0}^{\\infty}{\\frac{(-1)^k{2}^{4k}}{(2k!)}{x}^{2k}}",
            "-cos(4x)=\\sum_{k=0}^{\\infty}{\\frac{(-1)^{k+1}{2}^{4k}}{(2k!)}{x}^{2k}}",
            "1-cos(4x)=1+\\sum_{k=0}^{\\infty}{\\frac{(-1)^{k+1}{2}^{4k}}{(2k!)}{x}^{2k}}",
            "\\frac{1-cos(4x)}{2}=0.5+\\sum_{k=0}^{\\infty}{\\frac{(-1)^{k+1}{2}^{4k-1}}{(2k!)}{x}^{2k}}",
            "\\sin^2(2x)=0.5+\\sum_{k=0}^{\\infty}{\\frac{(-1)^{k+1}{2}^{4k-1}}{(2k!)}{x}^{2k}}"
        ]
        self.wait(2)
        self.play(FadeOut(self.hint))
        for equation in equations:
            self.play(Transform(titles[0], MathTex(equation).to_corner(UL)))
        self.wait()
        self.play(Transform(titles[0], MathTex(
            "\\sin^2(2x)=0.5+\\sum_{k=0}^{n}{\\frac{(-1)^{k+1}{2}^{4k-1}}{(2k!)}{x}^{2k}}").to_corner(UR)))
        self.play(titles[0].animate.scale(np.array((.5, .5, 0.0)), about_edge=UR))
        self.play(FadeIn(self.plot), FadeIn(self.sin))
        self.play(FadeIn(self.hint), Transform(self.hint, Tex("Let's visualize taylor series").move_to(3 * DOWN)))
        self.wait(2)
        self.play(FadeOut(self.hint))
        self.taylor = self.plot[0].plot(lambda x: (math.sin(2 * x) ** 2), color=PURPLE)
        text = MathTex(f"n=0")
        for iters in range(1, 15):
            self.play(Transform(text, MathTex(f"n={iters}").to_corner(UL)),
                      Transform(self.taylor, self.plot[0].plot(lambda x: (0.5 + sum(
                          map(lambda k: (-1) ** (k + 1) * (2 ** (4 * k - 1)) / math.factorial(2 * k) * (
                                  x ** (2 * k)),
                              range(iters)))), color=PURPLE, x_range=[-math.pi, math.pi])))
        print(self.plot[0].coords_to_point(math.pi, 0)[0])
        self.wait()
        rect = Rectangle(fill_color=DARK_BLUE, fill_opacity=.25, stroke_width=0, height=10,
                         width=self.plot[0].coords_to_point(math.pi / 2, 0)[0]).move_to(ORIGIN, aligned_edge=LEFT)
        self.play(FadeIn(rect))
        self.wait()
        self.play(FadeIn(self.hint), Transform(self.hint, MathTex(
            "\\text{It's enough to use range from 0 to} \\frac{\\pi}{2}").move_to(3 * DOWN)))
        self.wait(2)
        self.play(FadeOut(self.hint))
        self.play(FadeOut(rect), FadeOut(self.sin), FadeOut(titles[0]))
        self.wait()
        axes = Axes(
            x_range=[0, math.pi / 2, math.pi / 8],
            y_range=[0, 20, 1],
            y_axis_config={"numbers_to_include": np.arange(0, 20, 5)},
            y_length=self.camera.frame_width / 3,
            x_length=self.camera.frame_width / 2,
            axis_config={"color": GREEN},
            tips=False,
        )
        self.play(FadeIn(self.hint), Transform(self.hint,
                                               Tex("Now we can visualize number of elements you need to achieve epsilon accuracy at point x").move_to(
                                                   3 * DOWN).scale(.5)))
        self.wait(2)
        self.play(FadeOut(self.hint))
        axes.add(MathTex("\\frac{\\pi}{4}").next_to(axes.coords_to_point(math.pi / 4, 0), DOWN))
        self.play(Transform(self.plot[0], axes), FadeOut(self.plot[1]), FadeOut(self.taylor))
        for epsilon in range(1, 14):
            self.graph = axes.plot(lambda x: taylor.get_count(x, 10 ** (-epsilon)),
                                   x_range=[.0001, math.pi / 2 - 0.001, .0033], color=PURPLE)
            self.play(Transform(self.taylor, self.graph),
                      Transform(text, MathTex(f"\\varepsilon=10^{{-{epsilon}}}").to_corner(UL)))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(self.plot[0]), FadeOut(self.taylor), FadeIn(self.hint),
                  Transform(self.hint, Tex("Thanks for watching!!!")))
        self.wait(2)


config.quality = 'high_quality'
scene = SinAndCosFunctionPlot()
scene.render(preview=True)
