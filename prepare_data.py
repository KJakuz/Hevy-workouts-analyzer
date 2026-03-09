import pandas as pd

BODY_WEIGHT = 75

def main():
    input_file = "imported_workouts.csv"
    output_file = "workouts.csv"
    
    try:
        df = pd.read_csv(input_file)

        df['start_time'] = pd.to_datetime(df['start_time'])
        df['end_time'] = pd.to_datetime(df['end_time'])

        df['start_date'] = df['start_time'].dt.date
        df['start_hour'] = df['start_time'].dt.strftime('%H:%M')
        df['end_date'] = df['end_time'].dt.date
        df['end_hour'] = df['end_time'].dt.strftime('%H:%M')

        
        df['WeekDay'] = df['start_time'].dt.day_name()
        
        df['Year_month'] = df['start_time'].dt.strftime('%m-%Y')
        
        df['training_time'] = ((df['end_time'] - df['start_time']).dt.total_seconds() / 60).astype(int)
        
        df['Day of Week'] = df['start_time'].dt.weekday

        final_columns = [
            'start_date', 'start_hour', 'end_date', 'end_hour', 
            'exercise_title', 'set_index', 'set_type', 'weight', 'reps',
            'WeekDay', 'Year_month', 'training_time', 'Day of Week'
        ]
        
        df = df.rename(columns={'weight_kg': 'weight'})


        def calculate_actual_weight(row):
            title = str(row['exercise_title']).lower()
            if 'pushup' in title or 'push up' in title:
                return BODY_WEIGHT * 0.65
            elif 'pull up (assisted)' in title:
                return BODY_WEIGHT - row['weight']
            elif 'pull up' in title:
                return BODY_WEIGHT
            return row['weight']

        df['weight'] = df.apply(calculate_actual_weight, axis=1)
        
        df_final = df[final_columns]
        df_final.to_csv(output_file, index=False, sep=';', decimal=',')
        print("success")

    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()