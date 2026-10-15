from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    telemetry = {
        "battery": 45,
        "mission_status": "ВЫПОЛНЕНИЕ МИССИИ «ВЫНОСЛИВОСТЬ»",
        "sol": 1422,
        "coordinates": "18.38° N, 77.58° E (Кратер Езеро)",
        "environment": {
            "temperature": "-62°C",
            "radiation": "22 mSv/yr",
            "wind_speed": "7.2 m/s"
        },
        "subsystems": [
            {"name": "Генератор кислорода", "status": "ok", "value": 82},
            {"name": "Главный реактор", "status": "warning", "value": 94},  # Перегрев (>90)
            {"name": "Буровая установка", "status": "critical", "value": 40},       # ТРЕБУЕТ ВНИМАНИЯ
            {"name": "Навигационные камеры", "status": "ok", "value": 35},
            {"name": "Связь сверхвысокой частоты", "status": "ok", "value": 12},
            {"name": "Спектрометр", "status": "ok", "value": 54},
            {"name": "Модуль жизнеобеспечения", "status": "warning", "value": 91}    # Перегрев (>90)
        ]
    }

    return render_template(
        'index.html',
        battery=telemetry["battery"],
        subsystems=telemetry["subsystems"],
        mission_status=telemetry["mission_status"],
        sol=telemetry["sol"],
        coordinates=telemetry["coordinates"],
        environment=telemetry["environment"]
    )

if __name__ == '__main__':
    app.run(debug=True)