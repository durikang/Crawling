# data_processing.py
import pandas as pd

def adjust_columns(data, expected_columns):
    """
    데이터 열 개수를 맞추기 위해 누락된 열은 빈 문자열로 채우고,
    초과된 열은 잘라냅니다.
    """
    adjusted_data = []
    for row in data:
        if len(row) < expected_columns:
            row.extend([""] * (expected_columns - len(row)))  # 누락된 열 채우기
        elif len(row) > expected_columns:
            row = row[:expected_columns]  # 초과된 열 제거
        adjusted_data.append(row)
    return adjusted_data


def validate_and_create_df(data, columns):
    """
    주어진 데이터와 컬럼을 기반으로 데이터프레임을 생성하고,
    컬럼 길이와 데이터 길이가 맞지 않는 경우 적절한 조치를 취합니다.
    """
    # 데이터 열 개수 조정
    adjusted_data = adjust_columns(data, len(columns))
    # 데이터프레임 생성
    df = pd.DataFrame(adjusted_data, columns=columns)
    return df


def save_to_excel(file_path, data_frames, sheet_names):
    """
    여러 데이터프레임을 각기 다른 시트 이름으로 한 엑셀 파일에 저장합니다.
    """
    if not file_path.endswith(".xlsx"):
        file_path += ".xlsx"
    with pd.ExcelWriter(file_path) as writer:
        for df, sheet in zip(data_frames, sheet_names):
            df.to_excel(writer, sheet_name=sheet, index=False)


def preprocess_and_save_data(file_path, data_and_columns, sheet_names):
    """
    데이터를 사전 처리하고 엑셀로 저장합니다.

    :param file_path: 엑셀 파일 경로
    :param data_and_columns: (데이터, 컬럼) 튜플의 리스트
    :param sheet_names: 시트 이름 리스트
    """
    data_frames = []
    for data, columns in data_and_columns:
        df = validate_and_create_df(data, columns)
        data_frames.append(df)
    save_to_excel(file_path, data_frames, sheet_names)
