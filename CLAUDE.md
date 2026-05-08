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

## Testing Patterns

- **View 테스트**: pytest `capsys`로 stdout 캡처해 출력 내용 검증.
- **Controller 테스트**: `view.get_input`을 람다로 교체해 stdin 없이 입력 주입. `unittest.mock` 미사용.
- 각 테스트는 독립적인 `UserRepository` 인스턴스를 사용하므로 상태 공유 없음.
