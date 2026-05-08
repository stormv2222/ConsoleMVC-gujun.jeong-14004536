# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# 전체 테스트 실행
python -m pytest tests/ -v

# 단일 파일 테스트
python -m pytest tests/test_model.py -v

# 단일 테스트 함수 실행
python -m pytest tests/test_controller.py::test_create_user_adds_to_repository -v

# 앱 실행 (대화형 CLI)
python main.py
```

## Architecture

MVC 패턴의 의존성 방향: `main.py` → `Controller` → (`Model`, `View`)

- **Model** (`models/user.py`): `User` dataclass + `UserRepository` (인메모리 dict 저장소). 비즈니스 로직과 상태를 담당.
- **View** (`views/user_view.py`): 출력만 담당. `show_*` 메서드는 print, `get_input`은 input() 래핑.
- **Controller** (`controllers/user_controller.py`): `__init__`에서 `UserRepository`와 `UserView`를 주입받아 CRUD 흐름을 조율. `run()`이 메뉴 루프 진입점.
- **Wiring** (`main.py`): 세 레이어를 생성하고 Controller에 주입한 뒤 `run()` 호출.

## Skeleton Structure

이 저장소는 MVC 스켈레톤입니다. 각 파일의 클래스와 메서드 시그니처만 정의되어 있으며, 본문은 `pass`로 비워져 있습니다. 아래 구현 가이드를 참고해 채워 넣으세요.

### models/user.py

```
User (dataclass)
├── name: str
├── email: str
└── id: int  ← add/update 시 자동 부여, 직접 설정 금지

UserRepository
├── __init__()          : _store(dict), _next_id(int) 초기화
├── add(user) → User    : id 부여 후 저장, 저장된 user 반환
├── get(id) → User|None : id로 단건 조회, 없으면 None
├── get_all() → list    : 전체 목록 반환
├── update(id, **kwargs) → User|None : 필드 수정 (id 필드는 변경 불가)
└── delete(id) → bool   : 삭제 성공 True, 없으면 False
```

### views/user_view.py

```
UserView
├── show_user(user)         : 단건 출력
├── show_user_list(users)   : 목록 출력 (빈 경우 안내 메시지)
├── show_message(message)   : 일반 메시지 출력
└── get_input(prompt) → str : input() 래핑, strip() 적용
```

### controllers/user_controller.py

```
UserController
├── __init__(repository, view) : 의존성 주입
├── create_user()  : view로 입력 받아 repo에 저장
├── list_users()   : repo에서 조회 후 view로 출력
├── update_user()  : id 입력받아 repo 수정
├── delete_user()  : id 입력받아 repo 삭제
└── run()          : 메뉴 루프 (0 입력 시 종료)
```

### main.py

```
UserRepository, UserView, UserController 순으로 생성 후
controller.run() 호출
```

## Testing Patterns

- **View 테스트**: pytest `capsys`로 stdout 캡처해 출력 내용 검증.
- **Controller 테스트**: `view.get_input`을 람다로 교체해 stdin 없이 입력 주입. `unittest.mock` 미사용.
- 각 테스트는 독립적인 `UserRepository` 인스턴스를 사용하므로 상태 공유 없음.

> 완성된 샘플 구현은 `sample` 브랜치를 참고하세요.
