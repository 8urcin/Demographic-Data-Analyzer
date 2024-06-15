from demographic_data_analyzer import demographic_data_analyzer

if __name__ == "__main__":
    result = demographic_data_analyzer()
    for key, value in result.items():
        print(f"{key}: {value}")
