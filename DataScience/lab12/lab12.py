import random

import numpy
import pylab

# set line width
pylab.rcParams["lines.linewidth"] = 2  # Reduced for better point visibility
# set font size for titles
pylab.rcParams["axes.titlesize"] = 20
# set font size for labels on axes
pylab.rcParams["axes.labelsize"] = 20
# set size of numbers on x-axis
pylab.rcParams["xtick.labelsize"] = 16
# set size of numbers on y-axis
pylab.rcParams["ytick.labelsize"] = 16
# set size of ticks on x-axis
pylab.rcParams["xtick.major.size"] = 7
# set size of ticks on y-axis
pylab.rcParams["ytick.major.size"] = 7
# set size of markers, e.g., circles representing points
pylab.rcParams["lines.markersize"] = 5  # Set marker size
# set numpoints for legend
pylab.rcParams["legend.numpoints"] = 1


def sin_func(x):
    """Calculates the sine of x."""
    return numpy.sin(x)


def integration_simulation(func, low, high, num_samples, y_max=1.0):
    """
    Симуляцийн аргаар функцийн интеграл ойролцоолох.

    Args:
        func (callable): Интегралчлах функц.
        low (float): Интегралын доод хязгаар.
        high (float): Интегралын дээд хязгаар.
        num_samples (int): Симуляц явуулах sample-н тоо.
        y_max (float): y-н авч болох хамгийн дээд утга.
                       Энэ даалгаврын хүрээнд хамгийн бага y-н утгыг 0 гэж үзнэ.

    Returns:
        tuple: (estimated_integral, x_samples, y_samples, is_below)
               - estimated_integral (float): Интегралийн утга.
               - x_samples (list): Sample болгож авсан цэгүүдийн x тэнхлэгийн утгууд.
               - y_samples (list): Sample болгож авсан цэгүүдийн y тэнхлэгийн утгууд.
               - is_below (list): Sample цэгүүд func(x_samples[i]) функцийн доор
                                  оршиж байгаа эсэхийг илэрхийлэх boolean утгууд.
    """
    count_below_curve = 0
    x_samples = []
    y_samples = []
    is_below = []

    box_width = high - low
    box_area = box_width * y_max

    for _ in range(num_samples):
        # TODO: дараах алхмын дагуу хэрэгжүүлэх
        # 1. x, y утгыг өгсөн хязгаар дотор санамсаргүй үүсгэх
        # 2. санамсаргүй үүсгэсэн цэгүүд өгөгдсөн функцийн доор/дээр байгааг шалгаж, is_below-т хадгалах
        x = random.uniform(low, high)
        y = random.uniform(0, y_max)

        x_samples.append(x)
        y_samples.append(y)

        if y <= func(x):
            is_below.append(True)
            count_below_curve += 1
        else:
            is_below.append(False)
    estimated_integral = (count_below_curve / num_samples) * box_area

    return estimated_integral, x_samples, y_samples, is_below


# --- Параметрүүд ---
# TODO: параметрийг сайжруулж, симуляцын алдааг багасгаж, итгэлийн завсрыг (95%) +/- 0.05 дотор болгох
integration_low = 0  # интегралын доод хязгаар
integration_high = numpy.pi  # интегралын дээд хязгаар
num_simulation_samples = 10000  # нэг туршилтад үүсгэх цэгийн тоо
bounding_box_y_max = 1.0  # синус нь y тэнхлэгийн дагуу дээд тал нь 1 утга авах тул санамсаргүй үүсгэх цэгийн дээд хязгаарыг мөн 1 гэж авсан
num_trials = 1000  # туршилт явуулах тоо

# ---------------------------------------
# --- 1. Туршилтыг нэг удаа гүйцэтгэх ---
# ---------------------------------------

# --- Дүрсэлж үзүүлэх зорилгоор нэг удаагийн туршилт явуулах ---
integral_estimate, x_pts, y_pts, below = integration_simulation(
    sin_func,
    integration_low,
    integration_high,
    num_simulation_samples,
    bounding_box_y_max,
)

# --- Интегралын жинхэнэ утгыг олох ---
# санамж: sin(x) функцийн интеграл = -cos(x) + c
true_integral = -numpy.cos(integration_high) - (-numpy.cos(integration_low))

print(f"Туршилтын үр дүн ({num_simulation_samples} цэг): {integral_estimate:.6f}")
print(f"Интегралын жинхэнэ утга: {true_integral:.6f}")
print(f"Туршилтын үр дүнгийн алдаа: {abs(integral_estimate - true_integral):.6f}")

# PLOT 1: Синус функцийг зурах
pylab.figure(figsize=(10, 6))
x_vals = numpy.linspace(integration_low, integration_high, 200)
y_vals = sin_func(x_vals)
pylab.plot(x_vals, y_vals, label="sin(x)")
pylab.title("Синус функц")
pylab.xlabel("x")
pylab.ylabel("sin(x)")
pylab.xlim(integration_low, integration_high)
pylab.ylim(0, bounding_box_y_max * 1.1)
pylab.grid(True)
pylab.legend()
pylab.axhline(0, color="black", linewidth=0.5)
pylab.show()


# PLOT 2: Синус функц дээр туршилтын цэгүүдийг зурах
pylab.figure(figsize=(10, 6))
# Цэгүүдийг дээр доор байгаагаар нь салгах
x_below = [x_pts[i] for i in range(num_simulation_samples) if below[i]]
y_below = [y_pts[i] for i in range(num_simulation_samples) if below[i]]
x_above = [x_pts[i] for i in range(num_simulation_samples) if not below[i]]
y_above = [y_pts[i] for i in range(num_simulation_samples) if not below[i]]

# Функц
pylab.plot(x_vals, y_vals, label="sin(x)", color="black")
# Цэгүүд
pylab.scatter(x_below, y_below, color="blue", label="Муруйн доор орших цэг", s=5)
pylab.scatter(x_above, y_above, color="red", label="Муруйн дээр орших цэг", s=5)

pylab.title(f"Туршилтын цэгүүд ({num_simulation_samples})")
pylab.text(0, 1.05, f"интеграл\nest.={integral_estimate:.6f}, true={true_integral:.6f}")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.xlim(integration_low, integration_high)
pylab.ylim(0, bounding_box_y_max * 1.1)
pylab.grid(True)
pylab.legend(loc="upper right")
pylab.axhline(0, color="black", linewidth=0.5)
# Bounding box
pylab.plot(
    [
        integration_low,
        integration_high,
        integration_high,
        integration_low,
        integration_low,
    ],
    [0, 0, bounding_box_y_max, bounding_box_y_max, 0],
    "--",
    color="gray",
    label="Bounding Box",
)
pylab.show()


# ----------------------------------------
# --- 2. Туршилтыг олон удаа гүйцэтгэх ---
# ----------------------------------------
def run_trials(
    sin_func,
    integration_low,
    integration_high,
    bounding_box_y_max,
    num_trials,
    num_samples,
):
    """
    Симуляцийг олон удаа явуулах.

    Args:
        func (callable): Интегралчлах функц.
        low (float): Интегралын доод хязгаар.
        high (float): Интегралын дээд хязгаар.
        y_max (float): y-н авч болох хамгийн дээд утга.
                       Энэ даалгаврын хүрээнд хамгийн бага y-н утгыг 0 гэж үзнэ.
        num_trials (int): Нийт туршилтын тоо.
        num_samples (int): Симуляц явуулах sample-н тоо.

    Returns:
        estimates (list[float]): Бүх туршилтын үр дүнг агуулсан жагсаалт
    """
    estimates = []
    for i in range(num_trials):
        estimate, _, _, _ = integration_simulation(
            sin_func, integration_low, integration_high, num_samples, bounding_box_y_max
        )
        estimates.append(estimate)
    # TODO: өмнө нь хэрэгжүүлсэн integration_simulation функцийг num_trials удаа дуудаж утгыг estimates жагсаалтад нэмнэ
    return estimates


# num_trials тооны туршилт явуулах
all_estimates = run_trials(
    sin_func,
    integration_low,
    integration_high,
    bounding_box_y_max,
    num_trials,
    num_simulation_samples,
)

# Туршилтуудын үр дүнгээс дундаж болон стандарт хазайлтыг тооцох
mean_estimate = numpy.mean(all_estimates)
std_dev_estimate = numpy.std(all_estimates)
print(f"----- {num_trials} удаагийн туршилт ({num_simulation_samples} цэг) -----")
print(f"{num_trials} удаагийн туршилтын үр дүн:")
print(f"- Дундаж утга: {mean_estimate:.6f} +/- {std_dev_estimate * 1.96:.6f}")
print(f"- Стандарт хазайлт: {std_dev_estimate:.6f}")


# PLOT 3: Олон удаагийн туршилтын үр дүнгээс histogram зурж үзэх
pylab.figure(figsize=(10, 6))
pylab.hist(
    all_estimates,
    bins=30,
    density=True,
    alpha=0.7,
    label="Туршилтын үр дүнгийн тархалт",
)
# Туршилтын аргаар гаргаж авсан үр дүнгийн дундаж (улаан, тасархай босоо зураас)
pylab.axvline(
    float(mean_estimate),
    color="red",
    linestyle="dashed",
    linewidth=2,
    label=f"Туршилтын дундаж утга ({mean_estimate:.4f})",
)
# Интегралийн жинхэнэ утга (ногоон босоо зураас)
pylab.axvline(
    true_integral,
    color="green",
    linestyle="solid",
    linewidth=2,
    label=f"Жинхэнэ утга ({true_integral:.4f})",
)
# TODO: Энэ граф дээр туршилтын аргаар гаргаж авсан нийт үр дүнгийн
# ~68% (std*1), ~95% (std*1.96), ~99.7%(std*3) тус тус багтаасан босоо шулууныг
# дундаж утгын хоёр талд зурах (өөрөөр хэлбэл нийт үр дүнгийн 95%-г багтаасан дээд доод хязгаар шулуун).
# Босоо шулуун хэрхэн зурж байгааг дээрх дундаж утга зурсан кодоос харна уу.

pylab.title(
    f"Туршилтын аргаар олсон интегралын үр дүнгийн тархалт ({num_trials} туршилт)"
)
pylab.xlabel("Туршилтаар олсон интегралын утгууд")
pylab.ylabel("Density")
pylab.grid(True)

pylab.axvline(
    float(mean_estimate - 1.96 * std_dev_estimate),
    color="orange",
    linestyle=":",
    label="95% CI Lower",
)
pylab.axvline(
    float(mean_estimate + 1.96 * std_dev_estimate),
    color="orange",
    linestyle=":",
    label="95% CI Upper",
)


pylab.axvline(
    float(mean_estimate - std_dev_estimate),
    color="purple",
    linestyle="--",
    alpha=0.5,
    label="68% CI",
)
pylab.axvline(
    float(mean_estimate + std_dev_estimate), color="purple", linestyle="--", alpha=0.5
)
pylab.legend()
pylab.show()
